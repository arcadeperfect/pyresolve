import json
import re

from enum import Enum, auto
from pathlib import Path
from typing import Dict, Optional, Tuple

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


class SequenceBin:
    def __init__(
        self,
        name: str,                      # the name of the sequence, ie playblasts, comps
        sequence_root_path: Path,       # the filesystem path common to all shots
        sub_path: Path,                  # the filesystem path to traverse to find the shots, such as /renders or /ANM
        file_type: "FileType",          # enum representing the file type, ie DPX, EXR, MOV
        parent_bin: "Folder",           # the bin object in which the sequence bin resides
        kernel: "Kernel",               # the Resolve instance wrapper
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
        self.media_type = self.file_type.value
        self.kernel = kernel
        self.parent = parent_bin
        self._resolve_folder = None
        self.shot_bins: Dict[str, "ShotBin"] = {}

    @property
    def shot_paths(self) -> list[Path]:
        """A list of filesystem paths that correspond to shots in this sequence"""
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
        bins = {}
        for shot_path in self.shot_paths:
            shot_name = shot_path.name
            media_path = Path(shot_path) / self.sub_path
            if not media_path.is_dir():
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


class ShotBin:
    def __init__(
        self,
        name: str,                  # the name of the shot
        path: Path,                 # the filesystem path to this shot
        file_type: "FileType",      # enum representing the file type
        bin: Folder,                # reference to the resolve bin
        kernel: "Kernel",           # the Resolve instance wrapper
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
        self.folder = bin
        self.kernel = kernel
        pass

    @classmethod
    def from_media_pool_item(cls, item: MediaPoolItem, kernel: "Kernel") -> "ShotBin":

        """Instantiates a ShotBin object from a MediaPoolItem."""

        p = Path(item.GetClipProperty("File Path")) # type: ignore
        t = FileType[(p.suffix.upper().lstrip("."))]

        if t.value == MediaType.SEQUENCE:
            p = p.parent

        folder = find_clip_bin(item, kernel)

        if folder is None:
            raise ValueError("Could not find parent bin")

        return cls(item.GetName(), p.parent, t, folder, kernel)
    
    @classmethod
    def from_timeline_item(cls, item: TimelineItem, kernel: "Kernel") -> "ShotBin":

        return cls.from_media_pool_item(item.GetMediaPoolItem(), kernel)

    def populate_bin(self, depth: int):
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
                self.kernel.import_movie(clip_path, self.folder)

            if self.media_type == MediaType.SEQUENCE:
                self.kernel.import_sequence(
                    clip_path, clip_path.name, self.file_type.name.lower(), self.folder
                )

    @property 
    def newest_clip_in_bin(self) -> Optional[MediaPoolItem]:
        """
        Return the newest clip in the bin, currently just sorting by name
        TODO: sort by version or date
        """
        clip_list = self.list_clips_in_bin()
        if len(clip_list) == 0:
            return None

        if len(clip_list) == 0:
            return None
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
        return sorted([clip for clip in self.folder.GetClipList()], key=lambda x: x.GetName())

    def list_clip_paths_on_disk(self) -> list[Path]:
        if self.media_type == MediaType.MOVIE:
            return [p for p in self.path.iterdir() if p.is_file()]
        if self.media_type == MediaType.SEQUENCE:
            return [p for p in self.path.iterdir() if p.is_dir()]

        return []


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
            if (version := ShotBin.parse_version_number(clip.GetName()))
        }
    
    @property
    def versioned_clips_on_disk(self) -> dict[int, Path]:
        """
        Returns a dictionary of versioned clips available on disk.

        The keys are integers representing the parsed version numbers,
        and the values are the corresponding file paths on disk.

        Returns:
            dict[int, Path]: A dictionary mapping version numbers to file paths.
        """

        return {
            version: clip_path
            for clip_path in self.list_clip_paths_on_disk()
            if (version := ShotBin.parse_version_number(clip_path.name))
        }

    def version_up(
        self, timeline_item: TimelineItem, sort_mode: "SortMode"
    ) -> Optional[MediaPoolItem]:
        media_pool_item = timeline_item.GetMediaPoolItem()

        if sort_mode == SortMode.VERSIONPARSE:

            name = media_pool_item.GetName()
            current_version_number = ShotBin.parse_version_number(name)

            if current_version_number is None:
                return

            clips_in_bin = self.versioned_clips_in_folder

            keys = sorted(list(clips_in_bin.keys()))
            next_up = min((x for x in keys if x > current_version_number), default=None)

            if next_up is not None:
                new_clip = clips_in_bin[next_up]
            
            else:

                versions_on_disk = self.versioned_clips_on_disk
                keys = sorted(list(versions_on_disk.keys()))
                next_up = min((x for x in keys if x > current_version_number), default=None)
                # next_up = self.increment(current_version_number, keys)

                if next_up is None:
                    return

                found = None
                while found is None:
                    pth = versions_on_disk[next_up]
                    seqs = FileSequence.find_sequences_in_path(pth) # disover valid image sequences
                    if seqs:
                        found = seqs[0] # just going to assume the first one is the one we want (hopefully there is only one)
                        break
                    next_up = min((x for x in keys if x > next_up), default=None)
                    # next_up = self.increment(current_version_number, keys)
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

        return None

    def version_down(
            self, timeline_item: TimelineItem, sort_mode: "SortMode"
        ) -> Optional[MediaPoolItem]:
            
            """
            TODO better to always query the disk to get the next version,
            then check if it's already in the bin, rather than check the bin first
            and fall back to the disk

            both simpler and more robust, performance cost probably negligible
            """


            media_pool_item = timeline_item.GetMediaPoolItem()

            if sort_mode == SortMode.VERSIONPARSE:

                name = media_pool_item.GetName().split(".")[0]
                # current_version_number = ShotBin.parse_version_number(name)

                # if current_version_number is None:
                #     return
                if (current_version_number := ShotBin.parse_version_number(name)) is None:
                    return

                clips_in_bin = self.versioned_clips_in_folder

                keys = sorted(list(clips_in_bin.keys()))
                next = max((x for x in keys if x < current_version_number), default=None)

                if next is not None:
                    new_clip = clips_in_bin[next]
                
                else:

                    versions_on_disk = self.versioned_clips_on_disk
                    keys = sorted(list(versions_on_disk.keys()))
                    next = max((x for x in keys if x < current_version_number), default=None)
                    # next_up = self.increment(current_version_number, keys)

                    if next is None:
                        return

                    found = None
                    while found is None:
                        pth = versions_on_disk[next]
                        seqs = FileSequence.find_sequences_in_path(pth) # disover valid image sequences
                        if seqs:
                            found = seqs[0] # just going to assume the first one is the one we want (hopefully there is only one)
                            break
                        next = max((x for x in keys if x < current_version_number), default=None)
                        # next_up = self.increment(current_version_number, keys)
                        if next is None:
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
                

            return None

    @staticmethod
    def parse_version_number(name: str) -> Optional[int]:
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
        return self.media_storage.AddItemListToMediaPool(str(path))[0]

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


def retrieve_binpath(
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

    clip = travers_binpath(binpath, kernel)[1]
    return clip.GetMediaId() == item.GetMediaId()


def find_clip_bin(item: MediaPoolItem, kernel: Kernel) -> Folder:
    """
    First try to find the clip via a cached path,
    if that fails search for it and cache the path
    """

    binpath = retrieve_binpath(item, kernel)

    if binpath and validate_binpath(item, binpath, kernel):
        print("successfully located clip via cached path")
        return travers_binpath(binpath, kernel)[0]

    if (binpath is None) or (not validate_binpath(item, binpath, kernel)):
        print("failed to locate clip via cached path, performing search")
        new_binpath = find_folder_path(kernel.root_folder, item)
        folder = new_binpath[0]
        binpath = (new_binpath[1], new_binpath[2])
        encode_media_pool_item_binpath(item, binpath, kernel)
        return folder

    raise Exception(
        "Failed to find clip's bin"
    )  # There should be no scenario where we can't find it
