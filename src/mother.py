import re

from enum import Enum, auto
from pathlib import Path
from typing import Optional

# from lazy_prop import lazy_property
from file_sequence import FileSequence, Components

from _types import (
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


class SequenceBin:
    def __init__(
        self,
        name: str,
        path: Path,
        sub_path: str,
        file_type: "FileType",
        parent: "Folder",
        kernel: "Kernel",
    ):
        if not isinstance(name, str):
            raise TypeError("name must be a string")

        if not isinstance(path, Path):
            raise TypeError("path must be a Path object")

        if not isinstance(sub_path, str):
            raise TypeError("sub_path must be a string")

        if not isinstance(file_type, FileType):
            raise TypeError("file_type must be a FileType object")

        # if type(parent) is not BlackmagicFusion.PyRemoteObject:
        #     raise TypeError ...

        if not isinstance(kernel, Kernel):
            raise TypeError("kernel must be a Kernel object")

        self.name = name
        self.path = path
        self.sub_path = sub_path
        self.file_type = file_type
        self.media_type = self.file_type.value
        self.kernel = kernel
        self.parent = parent
        self._resolve_folder = None
        self.shot_bins = None

    @property
    def shot_paths(self) -> list[Path]:
        return [p for p in (self.path).iterdir() if p.is_dir()]

    @property
    def resolve_folder(self) -> Folder:
        if self._resolve_folder is None:
            self._resolve_folder = self.create_folder()
        return self._resolve_folder

    def create_folder(self) -> Folder:
        print("Creating resolve folder")
        for folder in self.parent.GetSubFolderList():
            if folder.GetName() == self.name:
                return folder

        return self.kernel.media_pool.AddSubFolder(self.parent, self.name)

    def create_shot_bins(self) -> dict[str, "ShotBin"]:
        bins = {}
        for shot_path in self.shot_paths:
            shot_name = shot_path.name
            media_path = Path(shot_path) / self.sub_path
            if not media_path.is_dir():
                continue
            resolve_folder = self.kernel.add_bin(shot_name, self.resolve_folder)
            bins[shot_name] = ShotBin(
                shot_name, media_path, self.file_type, resolve_folder, self.kernel
            )

        self.shot_bins = bins

        return bins


class ShotBin:
    def __init__(
        self,
        name: str,
        path: Path,
        file_type: "FileType",
        folder: Folder,
        kernel: "Kernel",
    ):
        # if not isinstance(name, str):
        #     raise TypeError("name must be a string")

        # if not isinstance(path, Path):
        #     raise TypeError("path must be a Path object")

        # if not isinstance(file_type, FileType):
        #     raise TypeError("file_type must be a FileType object")

        # # if type(parent) is not BlackmagicFusion.PyRemoteObject:
        # #     raise TypeError ...

        # if not isinstance(kernel, Kernel):
        #     raise TypeError("kernel must be a Kernel object")

        self.name = name
        self.path = path
        self.file_type = file_type
        self.media_type = self.file_type.value
        self.folder = folder
        self.kernel = kernel
        pass

    @classmethod
    def from_media_pool_item(cls, item: MediaPoolItem, kernel: "Kernel") -> "ShotBin":
        p = Path(item.GetClipProperty("File Path"))
        t = FileType[(p.suffix.upper().lstrip("."))]

        if t.value == MediaType.SEQUENCE:
            p = p.parent

        folder = kernel.find_parent_bin(item)

        if folder is None:
            raise ValueError("Could not find parent bin")

        return cls(item.GetName(), p.parent, t, folder, kernel)

    def populate_bin(self, depth: int):
        folder_contents = self.list_clip_names_in_bin()

        clip_paths = (
            self.list_clip_paths_on_disk()
            if depth < 1
            else self.list_clip_paths_on_disk()[-depth:]
        )

        for clip_path in clip_paths:
            if clip_path.stem in folder_contents:
                print(f"{clip_path.stem} already in bin")
                continue

            if self.media_type == MediaType.MOVIE:
                self.kernel.import_movie(clip_path, self.folder)

            if self.media_type == MediaType.SEQUENCE:
                self.kernel.import_sequence(
                    clip_path, clip_path.name, self.file_type.name.lower(), self.folder
                )

        # if self.media_type == MediaType.MOVIE:
        #     for clip_path in clip_paths:
        #         if clip_path.stem in folder_contents:
        #             print(f"{clip_path.stem} already in bin")
        #             continue

        #         self.kernel.import_movie(clip_path, self.folder)

        # if self.media_type == MediaType.SEQUENCE:
        #     for clip_path in clip_paths:
        #         if clip_path.stem in folder_contents:
        #             print(f"{clip_path.stem} already in bin")
        #             continue

        #         self.kernel.import_sequence(
        #             clip_path, clip_path.name, self.file_type.name.lower(), self.folder
        #         )

    def list_clip_names_in_bin(self) -> list[str]:
        return [clip.GetName().split(".")[0] for clip in self.folder.GetClipList()]

    def list_clips_in_bin(self) -> list[MediaPoolItem]:
        return [clip for clip in self.folder.GetClipList()]

    def list_clip_paths_on_disk(self) -> list[Path]:
        if self.media_type == MediaType.MOVIE:
            return [p for p in self.path.iterdir() if p.is_file()]
        if self.media_type == MediaType.SEQUENCE:
            return [p for p in self.path.iterdir() if p.is_dir()]

        return []

    def query_up(
        self, timeline_item: TimelineItem, sort_mode: "SortMode"
    ) -> Optional[MediaPoolItem]:
        media_pool_item = timeline_item.GetMediaPoolItem()

        if sort_mode == SortMode.VERSIONPARSE:

            name = media_pool_item.GetName()
            current_version = ShotBin.parse_version_name(name)

            if current_version is None:
                return

            clips_in_bin = {
                version: clip
                for clip in self.list_clips_in_bin()
                if (version := ShotBin.parse_version_name(clip.GetName()))
            }

            keys = sorted(list(clips_in_bin.keys()))
            next_up = min((x for x in keys if x > current_version), default=None)

            if next_up is not None:
                new_clip = clips_in_bin[next_up]
                timeline_item.AddTake(
                    new_clip,
                    timeline_item.GetSourceStartFrame(),
                    timeline_item.GetSourceEndFrame(),
                )

                timeline_item.SelectTakeByIndex(2)
                timeline_item.FinalizeTake()
                return new_clip

            versions_on_disk = {
                version: (clip_path)
                for clip_path in self.list_clip_paths_on_disk()
                if (version := ShotBin.parse_version_name(clip_path.name))
            }

            keys = sorted(list(versions_on_disk.keys()))
            next_up = min((x for x in keys if x > current_version), default=None)

            if next_up is None:
                return

            found = None
            while found is None:
                pth = versions_on_disk[next_up]
                seqs = FileSequence.find_sequences_in_path(pth)
                if seqs:
                    found = seqs[0]
                    break
                next_up = min((x for x in keys if x > next_up), default=None)
                if next_up is None:
                    break

            if not found:
                return

            new_clip = self.kernel.import_sequence(
                found.directory, found.prefix, found.extension, self.folder
            )

            if new_clip is None:
                return

            timeline_item.AddTake(
                new_clip,
                timeline_item.GetSourceStartFrame(),
                timeline_item.GetSourceEndFrame(),
            )

            timeline_item.SelectTakeByIndex(2)
            timeline_item.FinalizeTake()

            return new_clip

    # def import_clip(self, clip_path: Path) -> Optional[MediaPoolItem]:

    #     if self.media_type == MediaType.MOVIE:
    #         return self.kernel.import_movie(clip_path, self.folder)

    #     if self.media_type == MediaType.SEQUENCE:
    #         return self.kernel.import_sequence(
    #             clip_path.parent, clip_path.name, self.file_type.name.lower(), self.folder
    #         )

    def query_down(self, shot_stem):
        print(shot_stem)

    @staticmethod
    def parse_version_name(name: str) -> Optional[int]:
        name = name.split(".")[0]
        regex = r"_v(\d+)$"  # mathes any digits after the pattern _v
        match = re.search(regex, name)
        if match:
            return int(match.group(1))
        return None


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
    def active_media_item(self) -> Optional[MediaPoolItem]:
        """
        Returns the media pool item of the currently active timeline item, as defined by the playhead (not selection).
        """

        v = self.active_timeline_item

        if not v:
            return None

        return v.GetMediaPoolItem() or None

    def set_current_folder(self, bin: Folder):
        self.media_pool.SetCurrentFolder(bin)

    def add_bin(self, name: str, parent: Folder = None) -> Folder:
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
        return self.media_storage.AddItemListToMediaPool(str(path))

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
        print(f"Importing {seq.sequence_string} from {dir}")
        return self.media_pool.ImportMedia(
            [
                {
                    "FilePath": str(dir / name) + f".%0{seq.padding}d.{ext}",
                    "StartIndex": seq.first_frame,
                    "EndIndex": seq.last_frame,
                }
            ]
        )[0]

    def list_clip_names_in_folder(self, folder: Folder) -> list[str]:
        return [clip.GetName() for clip in folder.GetClipList()]

    # def add_bins(self, names, parent = None):
    #     if parent is None:
    #         parent = self.root_bin

    #     existing_bins = {bin.GetName():bin for bin in parent.GetSubFolderList()}

    #     bins = []
    #     for name in names:
    #         if name in existing_bins.keys():
    #             print(f"Bin {name} already exists")
    #             bins.append(existing_bins[name])
    #             continue
    #         bin = self.media_pool.AddSubFolder(parent, name)
    #         bins.append(bin)

    #     return bins

    def find_parent_bin(self, media_pool_item: MediaPoolItem) -> Optional[Folder]:
        # No function in the python api to get the parent bin of a clip, so we have to search

        def search_bins(folder, target_clip):
            clips = folder.GetClipList()
            for clip in clips:
                if clip.GetMediaId() == target_clip.GetMediaId():
                    return folder

            # Check subfolders
            subfolders = folder.GetSubFolderList()
            for subfolder in subfolders:
                result = search_bins(subfolder, target_clip)
                if result:
                    return result
            return None

        return search_bins(self.root_folder, media_pool_item)


class MediaType(Enum):
    MOVIE = auto()
    SEQUENCE = auto()


class FileType(Enum):
    DPX = MediaType.SEQUENCE
    EXR = MediaType.SEQUENCE
    PNG = MediaType.SEQUENCE
    MOV = MediaType.MOVIE
    MP4 = MediaType.MOVIE


class SortMode(Enum):
    VERSIONPARSE = auto()
    TIMESTAMP = auto()
