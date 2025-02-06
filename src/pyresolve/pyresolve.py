import json
import re
import platform

from enum import Enum, auto, unique
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# from lazy_prop import lazy_property
from .file_sequence import FileSequence, Components

from ._types import (
    Project,
    Timeline,
    MediaPool,
    TimelineItem,
    Folder,
    MediaPoolItem,
    MediaStorage,
    ProjectManager,
    Resolve,
    PyRemoteObject,
)

import os

# from initialize import find_clip_bin
import logging

logging.getLogger("pysequitur").setLevel(logging.WARNING)


class MediaType(Enum):
    MOVIE = auto()
    SEQUENCE = auto()


# @unique
# class FileType(Enum):
#     DPX = MediaType.SEQUENCE
#     EXR = MediaType.SEQUENCE
#     PNG = MediaType.SEQUENCE
#     MOV = MediaType.MOVIE
#     MP4 = MediaType.MOVIE

#     @property
#     def extension(self):
#         return self.name.lower()

#     @property
#     def media_type(self):
#         return self.value


@unique
class FileType(Enum):
    DPX = (MediaType.SEQUENCE, "dpx")
    EXR = (MediaType.SEQUENCE, "exr")
    PNG = (MediaType.SEQUENCE, "png")
    MOV = (MediaType.MOVIE, "mov")
    MP4 = (MediaType.MOVIE, "mp4")

    @property
    def extension(self):
        return self.name.lower()

    @property
    def media_type(self):
        return self.value[0]


class SortMode(Enum):
    VERSIONPARSE = auto()
    TIMESTAMP = auto()


class VersionChangeDirection(Enum):
    UP = auto()
    DOWN = auto()
    LATEST = auto()
    OLDEST = auto()


class SequenceBin:
    def __init__(
        self,
        name: str,  # the name of the sequence, ie playblasts, comps
        sequence_root_path: Path,  # the filesystem path common to all shots
        sub_path: Path,  # the filesystem path to traverse to find the shots, such as /renders or /ANM
        file_type: "FileType",  # enum representing the file type, ie DPX, EXR, MOV
        parent_bin: "Folder",  # the bin object in which the sequence bin resides
        kernel: "Kernel",  # the Resolve instance wrapper
    ):
        if not isinstance(name, str):
            raise TypeError("name must be a string")

        if not isinstance(sequence_root_path, Path):
            raise TypeError("path must be a pathlib.Path")

        if not isinstance(sub_path, Path):
            raise TypeError("sub_path must be a pathlib.Path")

        if not isinstance(file_type, FileType):
            raise TypeError("file_type must be a FileType object")

        if not isinstance(kernel, Kernel):
            raise TypeError("kernel must be a Kernel object")

        self.name = name
        self.path = sequence_root_path
        self.sub_path = sub_path
        self.file_type = file_type
        self.media_type = self.file_type.media_type
        # self.media_type = self.file_type.value
        self.kernel = kernel
        self.parent = parent_bin
        self._resolve_folder = None
        self.shot_bins: Dict[str, "ShotBin"] = {}

    @property
    def shot_paths(self) -> list[Path]:
        """A list of filesystem paths that correspond to shots in this sequence"""

        # print([p for p in (self.path).iterdir() if p.is_dir()])
        return [p for p in (self.path).iterdir() if p.is_dir()]

    @property
    def resolve_bin(self) -> Optional[Folder]:
        """A reference to the resolve bin"""
        if self._resolve_folder is None:
            self._resolve_folder = self.create_folder()
        return self._resolve_folder

    def create_folder(self) -> Folder:
        """Utility to create a sub bin instide the sequence bin"""
        print("Creating resolve folder")
        for folder in self.parent.GetSubFolderList():
            if folder.GetName() == self.name:
                return folder

        return self.kernel.media_pool.AddSubFolder(self.parent, self.name)

    def create_shot_bins(self) -> dict[str, "ShotBin"]:
        """Utility to batch create bins for all discovered shots"""
        print("Creating shot bins")
        # print(f"shot paths: {self.shot_paths}")
        bins = {}
        existing_bins = [bin.GetName() for bin in self.resolve_bin.GetSubFolderList()]
        for shot_path in self.shot_paths:
            shot_name = shot_path.name
            media_path = Path(shot_path) / self.sub_path

            if shot_name in existing_bins:
                print(f"Bin {shot_name} already exists")
                for bin in self.resolve_bin.GetSubFolderList():
                    if bin.GetName() == shot_name:
                        bins[shot_name] = ShotBin(
                            shot_name, media_path, self.file_type, bin, self.kernel
                        )
                        print(f"acquired existing bin {shot_name}")
                        continue

            if not media_path.is_dir():
                print(f"Media path {media_path} is not a directory, skipping")
                continue

            resolve_folder = self.kernel.add_bin(shot_name, self.resolve_bin)
            bins[shot_name] = ShotBin(
                shot_name, media_path, self.file_type, resolve_folder, self.kernel
            )

        self.shot_bins = bins

        return bins

    def populate_shot_bins(self, depth: int):
        if self.shot_bins is None:
            return

        for bin in self.shot_bins.values():
            bin.populate_bin(depth)

    def assemble_timeline(self, track: int = 1, handle: int = 0) -> Optional[Timeline]:
        """Assembles a timeline from the shot bins"""

        print("Assembling timeline")

        active_timeline = self.kernel.current_timeline

        if active_timeline is None:
            print("No active timeline")
            return None

        print(self.shot_bins.values())

        clipz = []

        for shot_bin in self.shot_bins.values():
            latest = shot_bin.newest_clip_in_bin
            if latest is None:
                continue
            # print(self.kernel.media_pool.AppendToTimeline(latest))

            # self.kernel.append_clip_to_timeline(latest, active_timeline, handle, track)

            clipz.append(latest)

        self.kernel.append_clips_to_timeline(clipz, active_timeline, handle, track)

        return active_timeline


class ShotBin:
    def __init__(
        self,
        shot_name: str,  # the name of the shot
        shot_path: Path,  # the filesystem path to this shot
        file_type: "FileType",  # enum representing the file type
        bin: Folder,  # reference to the resolve bin
        kernel: "Kernel",  # the Resolve instance wrapper
    ):
        self.name = shot_name
        self.path = shot_path
        self.file_type = file_type
        # self.media_type = self.file_type.value
        self.media_type = self.file_type.media_type
        self.folder = bin
        self.kernel = kernel
        pass

    @classmethod
    def from_media_pool_item(cls, item: MediaPoolItem, kernel: "Kernel") -> "ShotBin":
        """Instantiates a ShotBin object from a MediaPoolItem."""

        shot_path = Path(item.GetClipProperty("File Path"))  # type: ignore
        file_type = FileType[(shot_path.suffix.upper().lstrip("."))]

        # print(f"vvvv {file_type.media_type}")

        if file_type.media_type == MediaType.SEQUENCE:
            shot_path = shot_path.parent

        bin = find_clip_bin(item, kernel)

        if bin is None:
            raise ValueError("Could not find parent bin")

        # print(shot_path)

        return cls(item.GetName(), shot_path.parent, file_type, bin, kernel)

    @classmethod
    def from_timeline_item(cls, item: TimelineItem, kernel: "Kernel") -> "ShotBin":
        return cls.from_media_pool_item(item.GetMediaPoolItem(), kernel)

    def populate_bin(self, depth: int):
        print("Populating bin")
        folder_contents = self.list_clip_names_in_bin()

        clip_filesystem_paths = (
            self.list_clip_paths_on_disk()
            if depth < 1
            else self.list_clip_paths_on_disk()[-depth:]
        )

        for clip_path in clip_filesystem_paths:
            if clip_path.stem in folder_contents:
                print(f"{clip_path.stem} already in bin")
                continue

            if self.media_type == MediaType.MOVIE:
                # TODO handle case where movie doesn't have same name as folder

                self.kernel.import_movie(clip_path, self.folder)

            if self.media_type == MediaType.SEQUENCE:
                """
                the directory of the sequence should have the same name as the sequence, 
                however this is not necessarily enforced so I check for sequences with 
                the name derived from the path

                correct example:
                /path/to/renders/render_v001/render_v001.####.exr

                incorrect example:
                /path/to/renders/v001/render_v001.####.exr

                in the incorrect case, we will search first for a sequence by the name of v001.####.exr
                """
                clip_name = clip_path.name
                found_sequences = FileSequence.match_components_in_path(
                    Components(prefix=clip_name, extension=self.file_type.name.lower()),
                    clip_path.parent,
                )

                """
                if no sequences are found, as a fall back we search for valid sequences
                in the path and use the first one
                TODO use some more intelligent logic, or import all the valid sequences?
                """

                if len(found_sequences) == 0:  # no valid sequences
                    valid_sequences = FileSequence.find_sequences_in_path(clip_path)
                    if len(valid_sequences) != 0:
                        clip_name = valid_sequences[0].prefix
                    else:
                        continue

                item = self.kernel.import_sequence(
                    clip_path,  # the path to the sequence
                    clip_name,
                    self.file_type.name.lower(),
                    self.folder,
                )
                try:
                    if item:
                        item[0].SetClipProperty("Alpha mode", "None")
                except:
                    #TODO proper error handling
                    pass

    @property
    def newest_clip_in_bin(self) -> Optional[MediaPoolItem]:
        """
        Return the newest clip in the bin, currently just sorting by name
        """
        clip_list = self.list_clips_in_bin()
        if len(clip_list) == 0:
            return None

        if len(clip_list) == 0:
            return None

        for clip in clip_list:
            ShotBin._parse_version_number(clip.GetName())

        lambda x: ShotBin._parse_version_number(x.GetName())

        clip_list = sorted(
            clip_list, key=lambda x: ShotBin._parse_version_number(x.GetName()) or 0
        )  # sort by version

        return clip_list[-1]

    @property
    def oldest_clip_in_bin(self) -> Optional[MediaPoolItem]:
        """
        Return the newest clip in the bin, currently just sorting by name
        TODO: sort by version or date
        """
        clip_list = self.list_clips_in_bin()
        if len(clip_list) == 0:
            return None

        if len(clip_list) == 0:
            return None
        return clip_list[0]

    def list_clip_names_in_bin(self) -> list[str]:
        return [clip.GetName().split(".")[0] for clip in self.folder.GetClipList()]

    def list_clips_in_bin(self) -> list[MediaPoolItem]:
        return sorted(
            [clip for clip in self.folder.GetClipList()], key=lambda x: x.GetName()
        )

    def list_clip_paths_on_disk(self) -> list[Path]:
        if self.media_type == MediaType.MOVIE:
            return [p for p in self.path.iterdir() if p.is_file()]
        if self.media_type == MediaType.SEQUENCE:
            # print(self.path)
            return [p for p in self.path.iterdir() if p.is_dir()]

        raise ValueError(f"Invalid media type: {self.media_type}")

    @property
    def versioned_clips_in_folder(self) -> dict[int, MediaPoolItem]:
        """
        Returns a dictionary of versioned clips within the folder / bin.

        The keys are integers representing the parsed version numbers,
        and the values are the corresponding MediaPoolItem objects.

        Returns:
            dict[int, MediaPoolItem]: A dictionary mapping version numbers to MediaPoolItems.
        """

        return {
            version: clip
            for clip in self.folder.GetClipList()
            if (version := ShotBin._parse_version_number(clip.GetName()))
        }

    @property
    def versions_on_disk(self) -> dict[int, Path]:
        """
        Returns a dictionary of versioned clips available on disk.

        The keys are integers representing the parsed version numbers,
        and the values are the corresponding file paths on disk.

        Returns:
            dict[int, Path]: A dictionary mapping version numbers to file paths.
        """
        # print(self.list_clip_paths_on_disk())

        return {
            version: clip_path
            for clip_path in self.list_clip_paths_on_disk()
            if (version := ShotBin._parse_version_number(clip_path.name))
        }

    def deternine_media_type(self, item: MediaPoolItem) -> Optional["MediaType"]:
        # file = Path(item.GetClipProperty("File Path"))
        extension = os.path.splitext(item.GetClipProperty("File Name"))[-1]
        extension = extension.lstrip(".").upper()

        ft = FileType.__dict__.get(extension)

        if ft is None:
            return None

        mt = ft.media_type

        return mt

    def version_up(self, timeline_item: TimelineItem, sort_mode: "SortMode"):
        self._switch_version(
            timeline_item,
            sort_mode,
            lambda current, versions: min(
                (x for x in versions if x > current), default=None
            ),
        )

    def version_down(self, timeline_item: TimelineItem, sort_mode: "SortMode"):
        self._switch_version(
            timeline_item,
            sort_mode,
            lambda current, versions: max(
                (x for x in versions if x < current), default=None
            ),
        )

    def version_latest(self, timeline_item: TimelineItem, sort_mode: "SortMode"):
        print("version to latest")
        self._switch_version(
            timeline_item,
            sort_mode,
            lambda current, versions: max(versions)
            if max(versions) > current
            else None,
        )

    def version_oldest(self, timeline_item: TimelineItem, sort_mode: "SortMode"):
        self._switch_version(
            timeline_item,
            sort_mode,
            lambda current, versions: min(versions)
            if min(versions) < current
            else None,
        )


    def get_clip_timestamp(self, media_pool_item: MediaPoolItem):

        if not platform.system() == "Windows":
            raise NotImplementedError("Only Windows is currently supported.")

        if self.media_type == MediaType.MOVIE:
            p = Path(media_pool_item.GetClipProperty("File Path"))
            if p.exists():
                try:
                    t = p.stat().st_mtime
                    return t
                except Exception as e:
                    print(e)
            

        if self.media_type == MediaType.SEQUENCE:
            p = Path(media_pool_item.GetClipProperty("File Path")).parent
            # print(p)
            if p.exists():
                try:
                    t = p.stat().st_mtime
                    return t
                except Exception as e:
                    print(e)
            return None

        raise ValueError(f"Invalid media type: {self.media_type}")

        


    def _switch_version(
        self,
        timeline_item: TimelineItem,
        sort_mode: "SortMode",  # can be version parsing, or timestamp
        expression,  # lambda that determines the logic for deciding which version to switch to
    ) -> Optional[MediaPoolItem]:
        current_item = timeline_item.GetMediaPoolItem()

        print(sort_mode)


        # TODO this can be more dry
        # do ther vresion parsing according to sort mode
        # the rest of the logic should apply to either

        if sort_mode == SortMode.TIMESTAMP:

            current_time = self.get_clip_timestamp(current_item)
            # return None
            
            if current_time is None:
                print("Failed to get timestamp for current item")
                return None
                        
            versions_on_disk = {}
            for path in self.list_clip_paths_on_disk():
                if self.media_type == MediaType.MOVIE and path.is_file():
                    if t := path.stat().st_mtime:
                        versions_on_disk[t] = path
                elif self.media_type == MediaType.SEQUENCE and path.is_dir():
                    if t := path.stat().st_mtime:
                        versions_on_disk[t] = path
            
            versions_in_bin = {}
            for clip in self.folder.GetClipList():
                if t := self.get_clip_timestamp(clip):
                    versions_in_bin[t] = clip

            disk_version_keys = sorted(list(versions_on_disk.keys()))
            next_version = expression(current_time, disk_version_keys)
            expected_frame_count = int(current_item.GetClipProperty("Frames"))

            if next_version is None:
                return None

            new_clip = None

            if next_version in versions_in_bin.keys():
                print("found in bin, returning that")
                new_clip = versions_in_bin[next_version]
            else:
                media_type = self.deternine_media_type(current_item)
                print(media_type)
                if media_type == MediaType.MOVIE:
                    new_clip = self._handle_movie_version(
                        expression,
                        current_time,
                        current_item,
                        versions_on_disk,
                        disk_version_keys,
                        next_version,
                        expected_frame_count,
                    )
                elif media_type == MediaType.SEQUENCE:
                    new_clip = self._handle_image_sequence_version(
                        expression,
                        current_time,
                        current_item,
                        versions_on_disk,
                        disk_version_keys,
                        next_version,
                        expected_frame_count,
                    )
                else:
                    raise NotImplementedError(f"Unsupported media type: {media_type}")

            # return None

        elif sort_mode == SortMode.VERSIONPARSE:
            name = current_item.GetName()
            current_version_number = ShotBin._parse_version_number(name)

            if current_version_number is None:
                print("failed ot parse version number")
                return None

            versions_on_disk = self.versions_on_disk
            versions_in_bin = self.versioned_clips_in_folder
            disk_version_keys = sorted(list(versions_on_disk.keys()))

            next_version = expression(current_version_number, disk_version_keys)

            expected_frame_count = int(current_item.GetClipProperty("Frames"))

            if next_version is None:
                return None

            new_clip = None


            if next_version in versions_in_bin.keys():
                print("found in bin, returning that")
                new_clip = versions_in_bin[next_version]


            else:
                media_type = self.deternine_media_type(current_item)
                print(media_type)
                print("a")

                if media_type == MediaType.MOVIE:
                    new_clip = self._handle_movie_version(
                        expression,
                        current_version_number,
                        current_item,
                        versions_on_disk,
                        disk_version_keys,
                        next_version,
                        expected_frame_count,
                    )

                # IMAGE SEQUENCE
                elif media_type == MediaType.SEQUENCE:
                    print("b")
                    new_clip = self._handle_image_sequence_version(
                        expression,
                        current_version_number,
                        current_item,
                        versions_on_disk,
                        disk_version_keys,
                        next_version,
                        expected_frame_count,
                    )
                else:
                    raise NotImplementedError(f"Unsupported media type: {media_type}")

        else:
            raise NotImplementedError


        if new_clip is None:
            return None

        self._swap_clip(timeline_item, new_clip)

        return new_clip

        

    def _handle_image_sequence_version(
        self,
        expression,
        current_version_number,
        current_item,
        versions_on_disk,
        disk_version_keys,
        next_version,
        expected_frame_count,
    ):
        print("c")
        # versions_on_disk = self.versions_on_disk
        # disk_version_keys = sorted(list(versions_on_disk.keys()))
        # next_version = expression(current_version_number, disk_version_keys)
        valid_sequence = None

        sequence_path = versions_on_disk[next_version]
        print(sequence_path)
        seqs = FileSequence.find_sequences_in_path(
            sequence_path
        )  # disover valid image sequences

        while valid_sequence is None:

            # disover valid image sequences
            if seqs:
                sequence = seqs[0]  # just going to assume the first one is the one we want (hopefully there is only one valid sequence in the folder)

                print(f"{sequence.frame_count} == {expected_frame_count}")

                valid_sequence = sequence

                break
                # if sequence.frame_count == expected_frame_count:  # TODO use with frame validation method
                #     valid_sequence = sequence
                #     break
                # else:
                #     print("frames didn't match")

            next_version = expression(next_version, disk_version_keys)

            if next_version is None:
                break

        if not valid_sequence:
            return None

        print("d")

        new_clip = self.kernel.import_sequence(
            valid_sequence.directory,
            valid_sequence.prefix,
            valid_sequence.extension,
            self.folder,
        )[0]

        print(f"returning new clip to {new_clip}")

        return new_clip

    def _handle_movie_version(
        self,
        expression,
        current_version_number,
        current_item,
        versions_on_disk,
        disk_version_keys,
        next_version,
        expected_frame_count,
    ):
        print("handling movie version")

        # versions_on_disk = self.versions_on_disk
        # disk_version_keys = sorted(list(versions_on_disk.keys()))
        # next_version = expression(current_version_number, disk_version_keys)
        print(f"next version 1: {next_version}")
        valid_clip = None
        while valid_clip is None:
            clip_path = versions_on_disk[next_version]
            if clip_path.is_file():
                temp_clip = self.kernel.import_movie(clip_path, self.folder)

                if self._validate_frame_count(
                    int(temp_clip.GetClipProperty("Frames")), expected_frame_count
                ):
                    valid_clip = self.kernel.import_movie(clip_path, self.folder)
                    break
                else:
                    print("temp clip frame range invalid")
                    self.kernel.remove_clip_from_media_pool(temp_clip)
                    valid_clip = None
            next_version = expression(next_version, disk_version_keys)
            print(f"next version 2: {next_version}")

            if next_version is None:
                break

        if not valid_clip:
            return None

        return valid_clip
        # new_clip = valid_clip

    def _swap_clip(self, timeline_item: TimelineItem, new_clip: MediaPoolItem):
        timeline = self.kernel.current_timeline

        if timeline is None:
            return

        if timeline is not None:
            playhead = timeline.GetCurrentTimecode()
        else:
            playhead = None

        # TODO handle frame range mismatch

        (start, end), (in_, out) = get_timeline_item_frame_info(timeline_item)

        first, last, duration = get_media_pool_item_frame_info(new_clip)

        track_index = int(timeline_item.GetTrackTypeAndIndex()[1])

        if duration == 1:

            print(f"duration: {duration}")
            print(f"start: {start}")
            print(f"end: {end}")
            print(f"first: {first}")
            print(f"last: {last}")
            print(f"in: {in_}")
            print(f"out: {out}")
            print(f"track index: {track_index}")

            self.kernel.remove_clip_from_timeline(timeline_item)
            result = self.kernel.append_clip_to_timeline_in_out(
                new_clip,
                timeline,
                first, #clip in
                last,  #clip out
                start,   #track in
                end,   #track out
                track_index
            )

            print(result)

            return

        timeline_item.AddTake(
            new_clip,
            timeline_item.GetSourceStartFrame(),
            timeline_item.GetSourceEndFrame(),
        )

        timeline_item.SelectTakeByIndex(2)
        timeline_item.FinalizeTake()

        if playhead and timeline:
            timeline.SetCurrentTimecode(playhead)

    def _validate_frame_count(self, expected, candidate) -> bool:
        # return expected == candidate
        return True

    @staticmethod
    def _parse_version_number(name: str) -> Optional[int]:
        name = name.split(".")[0]

        # Match _v123
        regex = r"_v(\d+)$"
        match = re.search(regex, name)
        if match:
            return int(match.group(1))

        # Match v123
        regex = r"^v(\d+)$"
        match = re.search(regex, name)
        if match:
            return int(match.group(1))

        # Match any trailing numbers
        regex = r".*?(\d+)$"
        match = re.search(regex, name)
        if match:
            return int(match.group(1))

        print(f"Could not parse version number from {name}")

        return None

    @staticmethod
    def version_up_item(item: TimelineItem, kernel: "Kernel"):
        shot_bin = ShotBin.from_timeline_item(item, kernel)
        return shot_bin.version_up(item, SortMode.VERSIONPARSE)

    @staticmethod
    def version_down_item(item: TimelineItem, kernel: "Kernel"):
        shot_bin = ShotBin.from_timeline_item(item, kernel)
        return shot_bin.version_down(item, SortMode.VERSIONPARSE)

    @staticmethod
    def version_oldest_item(item: TimelineItem, kernel: "Kernel"):
        shot_bin = ShotBin.from_timeline_item(item, kernel)
        return shot_bin.version_oldest(item, SortMode.VERSIONPARSE)

    @staticmethod
    def version_latest_item(item: TimelineItem, kernel: "Kernel"):
        shot_bin = ShotBin.from_timeline_item(item, kernel)
        return shot_bin.version_latest(item, SortMode.VERSIONPARSE)


class Kernel:
    def __init__(self, resolve: Resolve):
        self.resolve = resolve

    # @lazy_property
    @property
    def project(self) -> Project:
        return self.resolve.GetProjectManager().GetCurrentProject()

    # @lazy_property
    @property
    def current_timeline(self) -> Optional[Timeline]:
        """
        Returns the currently loaded timeline.

        """
        return self.project.GetCurrentTimeline()

    # @lazy_property
    @property
    def media_pool(self) -> MediaPool:
        return self.resolve.GetProjectManager().GetCurrentProject().GetMediaPool()

        # return self.project.GetMediaPool()

    # @lazy_property
    @property
    def media_storage(self) -> MediaStorage:
        return self.resolve.GetMediaStorage()

    # @lazy_property
    @property
    def root_folder(self) -> Folder:
        return self.media_pool.GetRootFolder()

    @property
    def active_timeline_item(self) -> Optional[TimelineItem]:
        """
        Returns the currently active timeline item, as defined by the playhead (not selection).
        """

        v = self.current_timeline

        if not v:
            return None

        return v.GetCurrentVideoItem() or None

        # return self.current_timeline.GetCurrentVideoItem() or None

    @property
    def active_media_pool_item(self) -> Optional[MediaPoolItem]:
        """
        Returns the media pool item of the currently active timeline item, as defined by the playhead (not selection).
        """

        v = self.active_timeline_item

        if not v:
            return None

        return v.GetMediaPoolItem() or None

    @property
    def active_timeline_items(self) -> Optional[List[TimelineItem]]:
        current_timeline = self.current_timeline

        if not current_timeline:
            return None

        active_timeline_item = current_timeline.GetCurrentVideoItem()

        if active_timeline_item is None:
            return None

        track_type, track_index = active_timeline_item.GetTrackTypeAndIndex()
        if track_type is None or track_index is None:
            return None

        return current_timeline.GetItemListInTrack(track_type, track_index)

    def get_video_items_in_track(self, track) -> Optional[List[TimelineItem]]:
        c = self.current_timeline

        if not c:
            return None

        return c.GetItemListInTrack("video", track)

    def set_current_folder(self, bin: Folder):
        self.media_pool.SetCurrentFolder(bin)

    def add_bin(self, name: str, parent: Optional[Folder]) -> Folder:
        if parent is None:
            parent = self.root_folder
        if parent is None:
            raise ValueError("Could not find root folder")
        existing_bins = {bin.GetName(): bin for bin in parent.GetSubFolderList()}
        if name in existing_bins.keys():
            print(f"Bin {name} already exists")
            return existing_bins[name]
        return self.media_pool.AddSubFolder(parent, name)

    def import_movie(self, path: Path, folder: Folder) -> MediaPoolItem:
        print(f"Importing {path}")
        self.set_current_folder(folder)
        new_item = self.media_storage.AddItemListToMediaPool(str(path))[0]
        if new_item:
            try:
                new_item.SetClipProperty("Alpha Mode", "Ignore")
            except Exception:
                #TODO handle exception
                pass
        return new_item

    def import_sequence(
        self, dir: Path, name: str, ext: str, folder: Folder
    ) -> Optional[MediaPoolItem]:
        """
        Imports a sequence of files into the media pool. First and last frames are inferred.

        Args:
            dir (Path): The directory in which the sequence is located.
            name (str): The name of the sequence without extension or frame number.
            ext (str): The extension of the sequence files.
            folder (Folder): The folder in which to place the imported sequence.

        Returns:
            Optional[MediaPoolItem]: The imported media pool item, or None if no sequence is found.
        """
        self.set_current_folder(folder)

        seqs = FileSequence.match_components_in_path(Components(extension=ext), dir)

        if len(seqs) == 0:
            return None

        seq = seqs[0]
        # print(f"Importing {seq.sequence_string} from {dir}")

        p = str(dir / name) + f".%0{seq.padding}d.{ext}"
        # print(p)
        # print(name)

        l = self.media_pool.ImportMedia(
            [
                {
                    "FilePath": str(dir / name) + f".%0{seq.padding}d.{ext}",
                    "StartIndex": seq.first_frame,
                    "EndIndex": seq.last_frame,
                }
            ]
        )

        for s in l:
            try:
                s.SetClipProperty("Alpha Mode", "Ignore")
            except Exception:
                #TODO handle exception
                pass

        return l

    def remove_clip_from_media_pool(self, clip: MediaPoolItem):
        self.media_pool.DeleteClips([clip])

    def remove_clip_from_timeline(self, clip: TimelineItem):
        if self.current_timeline is None:
            return

        self.current_timeline.DeleteClips([clip], False)

    def list_clip_names_in_folder(self, folder: Folder) -> list[str]:
        return [clip.GetName() for clip in folder.GetClipList()]

    def get_existing_track_indices(self) -> list[int]:
        timeline = self.current_timeline
        if timeline is None:
            return []
        tracks = timeline.GetTrackCount("video")
        if tracks is None:
            return []
        return list(range(1, tracks + 1))

    # def append_clip_to_timeline(
    #     self,
    #     clip: MediaPoolItem,
    #     timeline: Timeline,
    #     clip_in: int,
    #     clip_out: int,
    #     track_in: int,
    #     track_out: int,
    #     track_index: int,
    # ):
    #     self.project.SetCurrentTimeline(timeline)
    #     clipInfo = {
            
    #         "mediaPoolItem": clip,
    #     }
    def append_clip_to_timeline_in_out(
        self,
        clip: MediaPoolItem,
        timeline: Timeline,
        clip_in: int,
        clip_out: int,
        track_in: int,
        track_out: int,
        track_index: int,
    ):
        self.project.SetCurrentTimeline(timeline)
        
        print(f"Clip in: {clip_in}")
        print(f"Clip out: {clip_out}")
        print(f"Track in: {track_in}")
        print(f"Track out: {track_out}")


        # Calculate source and target durations
        source_duration = clip_out - clip_in + 1
        target_duration = track_out - track_in + 1
        
        clipInfo = {
            "mediaPoolItem": clip,
            # "startFrame": 533,
            # "endFrame": 533,
            "recordFrame": track_in,
            "trackIndex": track_index,
            # "mediaType": 1
        }
        
        # Get the media pool and append the clip
        mediaPool = self.project.GetMediaPool()
        timeline_items = mediaPool.AppendToTimeline([clipInfo])
        
        if timeline_items:
            timeline_item = timeline_items[0]
            print(f"Timeline item: {timeline_item}")
            # Calculate speed adjustment needed
            speed_factor = source_duration / target_duration
            print(f"Speed factor: {speed_factor}")
            # Set retiming properties
            # timeline_item.SetProperty("RetimeProcess", self.resolve.)
            print(timeline_item.SetProperty("Speed", speed_factor))
            
            return timeline_items
        
        return None

    def append_clip_to_timeline_with_handles(
        self,
        clip: MediaPoolItem,
        timeline: Timeline,
        handle: int = 0,
        track_index: Optional[int] = None,
    ):
        self.project.SetCurrentTimeline(timeline)

        if timeline is None:
            return

        a = int(clip.GetClipProperty("Start"))
        b = int(clip.GetClipProperty("End"))
        start = a + handle
        end = b - handle
        start = min(start, b - 1)
        end = max(start + 1, end)

        print(start, end)

        print(timeline.GetStartFrame())

        # print(timeline.Fr())

        if track_index:
            print(f"track index: {track_index}")
            self.media_pool.AppendToTimeline(
                [
                    {
                        "mediaPoolItem": clip,
                        "startFrame": start,  # 5 frames before clip start
                        "endFrame": end,  # 5 frames after clip end
                        "trackIndex": 1,
                    }
                ]
            )

        else:
            self.media_pool.AppendToTimeline(
                [
                    {
                        "mediaPoolItem": clip,
                        "startFrame": start,  # 5 frames before clip start
                        "endFrame": end,  # 5 frames after clip end
                    }
                ]
            )

    def append_clips_to_timeline(
        self,
        clips: list[MediaPoolItem],
        timeline: Timeline,
        handle: int = 0,
        track_index: Optional[int] = None,
    ):
        self.project.SetCurrentTimeline(timeline)

        if timeline is None:
            return

        append_dict_list = []

        for clip in clips:
            a = int(clip.GetClipProperty("Start"))
            b = int(clip.GetClipProperty("End"))
            start = a + handle
            end = b - handle
            start = min(start, b - 1)
            end = max(start + 1, end)

            print(start, end)

            print(timeline.GetStartFrame())

            # print(timeline.Fr())

            if track_index:
                append_dict_list.append(
                    {
                        "mediaPoolItem": clip,
                        "startFrame": start,  # 5 frames before clip start
                        "endFrame": end,  # 5 frames after clip end
                        "trackIndex": track_index,
                    }
                )

            else:
                append_dict_list.append(
                    {
                        "mediaPoolItem": clip,
                        "startFrame": start,  # 5 frames before clip start
                        "endFrame": end,  # 5 frames after clip end
                    }
                )

        self.media_pool.AppendToTimeline(append_dict_list)


def find_folder_path(
    root: Folder, media_pool_item: MediaPoolItem
) -> Tuple[Folder, list[int], int]:
    path = []

    def search_bins(folder: Folder, target_clip: MediaPoolItem, path: list[int]):
        clips = folder.GetClips()
        for index, clip in clips.items():
            if clip.GetMediaId() == target_clip.GetMediaId():
                return (folder, path, index)

        subfolders = folder.GetSubFolders()
        for index, folder in subfolders.items():
            if not index:
                continue
            result = search_bins(folder, target_clip, [*path, index])
            if result:
                return result
        return None

    result = search_bins(root, media_pool_item, path)

    if result is None:
        raise Exception("Could not find bin path")

    return result


def encode_media_pool_item_binpath(
    item: MediaPoolItem, binpath: Tuple[list[int], int], kernel: Kernel
) -> bool:
    """
    Discover the bin path of the item with recursive search and encode
    in the metadata of the MediaPoolItem
    """

    # folder_path = find_folder_path(kernel.root_folder, item)

    if binpath is None:
        return False

    json_string = json.dumps({"folder_path": binpath[0], "clip_index": binpath[1]})

    return item.SetThirdPartyMetadata({"path": json_string})


def retrieve_binpath_from_metadata(
    item: MediaPoolItem, kernel: Kernel
) -> Optional[Tuple[list[int], int]]:
    json_string = item.GetThirdPartyMetadata("path")

    if json_string is None:
        return None

    if json_string == "":
        return None

    try:
        data = json.loads(json_string)

        data = (data["folder_path"], data["clip_index"])
        if isinstance(data[0], list) and isinstance(data[1], int):
            return data
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

    return None


def travers_binpath(
    binpath: Tuple[list[int], int], kernel: Kernel
) -> Tuple[Folder, MediaPoolItem]:  # type: ignore
    root = kernel.root_folder
    for index in binpath[0]:
        root = root.GetSubFolders()[index]  # type: ignore

    clip = root.GetClips()[binpath[1]]  # type: ignore
    return (root, clip)


def validate_binpath(
    item: MediaPoolItem, binpath: Tuple[list[int], int], kernel: Kernel
) -> bool:
    # binpath = access_media_pool_item_binpath(item, kernel)

    if binpath is None:
        return False

    if len(binpath) != 2:
        return False

    if len(binpath[0]) == 0:
        return False

    clip = travers_binpath(binpath, kernel)[1]
    return clip.GetMediaId() == item.GetMediaId()


def find_clip_bin(item: MediaPoolItem, kernel: Kernel) -> Folder:
    """
    First try to find the clip via a cached path,
    if that fails search for it and cache the path
    """

    binpath = retrieve_binpath_from_metadata(item, kernel)

    # print(binpath)

    if binpath and validate_binpath(item, binpath, kernel):
        # print("successfully located clip via cached path")
        return travers_binpath(binpath, kernel)[0]

    if (binpath is None) or (not validate_binpath(item, binpath, kernel)):
        # print("failed to locate clip via cached path, performing search")
        new_binpath = find_folder_path(kernel.root_folder, item)
        folder = new_binpath[0]
        binpath = (new_binpath[1], new_binpath[2])
        encode_media_pool_item_binpath(item, binpath, kernel)
        return folder

    raise Exception(
        "Failed to find clip's bin"
    )  # There should be no scenario where we can't find it


def version_up_track(track_index: int, kernel: Kernel):
    timeline = kernel.current_timeline
    if timeline is None:
        return
    videoItems = timeline.GetItemListInTrack("video", track_index)
    if videoItems is None:
        return
    for item in videoItems:
        ShotBin.version_up_item(item, kernel)


def version_down_track(track_index: int, kernel: Kernel):
    timeline = kernel.current_timeline
    if timeline is None:
        return
    videoItems = timeline.GetItemListInTrack("video", track_index)
    if videoItems is None:
        return
    for item in videoItems:
        ShotBin.version_down_item(item, kernel)


def version_latest_track(track_index: int, kernel: Kernel):
    timeline = kernel.current_timeline
    if timeline is None:
        return
    videoItems = timeline.GetItemListInTrack("video", track_index)
    if videoItems is None:
        return
    for item in videoItems:
        ShotBin.version_latest_item(item, kernel)


def version_oldest_track(track_index: int, kernel: Kernel):
    timeline = kernel.current_timeline
    if timeline is None:
        return
    videoItems = timeline.GetItemListInTrack("video", track_index)
    if videoItems is None:
        return
    for item in videoItems:
        ShotBin.version_oldest_item(item, kernel)


def version_up_tracks(track_indices: list[int], kernel: Kernel):
    existing_tracks = kernel.get_existing_track_indices()
    for track_index in track_indices:
        if track_index not in existing_tracks:
            continue
        version_up_track(track_index, kernel)


def version_down_tracks(track_indices: list[int], kernel: Kernel):
    existing_tracks = kernel.get_existing_track_indices()
    for track_index in track_indices:
        if track_index not in existing_tracks:
            continue
        version_down_track(track_index, kernel)


def version_latest_tracks(track_indices: list[int], kernel: Kernel):
    existing_tracks = kernel.get_existing_track_indices()
    for track_index in track_indices:
        if track_index not in existing_tracks:
            continue
        version_latest_track(track_index, kernel)


def version_oldest_tracks(track_indices: list[int], kernel: Kernel):
    existing_tracks = kernel.get_existing_track_indices()
    for track_index in track_indices:
        if track_index not in existing_tracks:
            continue
        version_oldest_track(track_index, kernel)


def get_timeline_item_frame_info(
    timeline_item: TimelineItem,
) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Returns a tuple of two tuples of two integers each. The first tuple is
    (start_frame, end_frame) of the timeline item in the timeline, and the
    second tuple is (start_frame, end_frame) of the media pool item source
    clip in the timeline item.

    Args:
        timeline_item (TimelineItem): The timeline item to get frame info for

    Returns:
        Tuple[Tuple[int, int], Tuple[int, int]]:
        First tuple is start and end frame of timeline
        Second tuple is in and out frame of source clip
    """
    timeline_start_frame = int(timeline_item.GetStart())
    timeline_end_frame = int(timeline_item.GetEnd())
    source_start_frame = timeline_item.GetSourceStartFrame()
    source_end_frame = timeline_item.GetSourceEndFrame()

    return (
        (timeline_start_frame, timeline_end_frame),
        (source_start_frame, source_end_frame),
    )


def get_media_pool_item_frame_info(
    m: MediaPoolItem,
) -> Tuple[
    int,  # first_frame_on_disk
    int,  # last_frame_on_disk
    int,  # duration
]:
    duration = m.GetClipProperty("frames")
    first_frame_on_disk = m.GetClipProperty("Start")
    last_frame_on_disk = m.GetClipProperty("End")

    return int(first_frame_on_disk), int(last_frame_on_disk), int(duration)
