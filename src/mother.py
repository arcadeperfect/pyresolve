from enum import Enum, auto
from pathlib import Path
from lazy_prop import lazy_property

import os


class SequenceBin:
    def __init__(
        self,
        name: str,
        path: Path,
        sub_path: str,
        file_type: "FileType",
        parent,
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
    def shot_paths(self):
        return [p for p in (self.path).iterdir() if p.is_dir()]

    @property
    def resolve_folder(self):
        if self._resolve_folder is None:
            self._resolve_folder = self.create_resolve_folder()
        return self._resolve_folder

    def create_resolve_folder(self):
        print("Creating resolve folder")
        for folder in self.parent.GetSubFolderList():
            if folder.GetName() == self.name:
                return folder

        return self.kernel.media_pool.AddSubFolder(self.parent, self.name)

    def create_shot_bins(self):
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
        resolve_folder,
        kernel: "Kernel",
    ):
        
        if not isinstance(name, str):
            raise TypeError("name must be a string")

        if not isinstance(path, Path):
            raise TypeError("path must be a Path object")

        if not isinstance(file_type, FileType):
            raise TypeError("file_type must be a FileType object")

        # if type(parent) is not BlackmagicFusion.PyRemoteObject:
        #     raise TypeError ...

        if not isinstance(kernel, Kernel):
            raise TypeError("kernel must be a Kernel object")

        self.name = name
        self.path = path
        self.file_type = file_type
        self.media_type = self.file_type.value
        self.folder = resolve_folder
        self.kernel = kernel

    # def populate(self, depth):

    def populate_bin(self, depth):
        self.kernel.set_current_folder(self.folder)

        folder_contents = self.list_clip_names_in_bin()

        if self.media_type == MediaType.MOVIE:
            for clip_path in self.list_clip_paths_on_disk()[-depth:]:
                if clip_path.name in folder_contents:
                    continue

                self.kernel.import_movie(clip_path)

        if self.media_type == MediaType.SEQUENCE:
            for clip_path in self.list_clip_paths_on_disk()[-depth:]:
                if clip_path.name in folder_contents:
                    continue

                self.kernel.import_sequence(
                    clip_path, clip_path.name, self.file_type.name.lower()
                )

    def list_clip_names_in_bin(self):
        return [clip.GetName() for clip in self.folder.GetClipList()]

    def list_clip_paths_on_disk(self):
        if self.media_type == MediaType.MOVIE:
            return [p for p in self.path.iterdir() if p.is_file()]
        elif self.media_type == MediaType.SEQUENCE:
            return [p for p in self.path.iterdir() if p.is_dir()]

    def query_up(self, shot_stem):
        print(shot_stem)

    def query_down(self, shot_stem):
        print(shot_stem)


class Kernel:
    def __init__(self, resolve):
        self.resolve = resolve

    @lazy_property
    def project(self):
        return self.resolve.GetProjectManager().GetCurrentProject()

    @lazy_property
    def current_timeline(self):
        return self.project.GetCurrentTimeline()

    @lazy_property
    def media_pool(self):
        return self.project.GetMediaPool()

    @lazy_property
    def media_storage(self):
        return self.resolve.GetMediaStorage()

    @lazy_property
    def root_bin(self):
        return self.media_pool.GetRootFolder()

    @property
    def active_timeline_item(self):
        return self.current_timeline.GetCurrentVideoItem()

    @property
    def active_media_item(self):
        return self.active_timeline_item.GetMediaPoolItem()

    def set_current_folder(self, bin):
        self.media_pool.SetCurrentFolder(bin)

    def add_bin(self, name, parent=None):
        if parent is None:
            parent = self.root_bin
        existing_bins = {bin.GetName(): bin for bin in parent.GetSubFolderList()}
        if name in existing_bins.keys():
            print(f"Bin {name} already exists")
            return existing_bins[name]
        return self.media_pool.AddSubFolder(parent, name)

    def import_movie(self, path: Path):
        print(f"Importing {path}")
        return self.media_storage.AddItemListToMediaPool(str(path))

    def import_sequence(self, dir: Path, name: str, ext: str):


        files = sorted(list(dir.glob(f"*.{ext}")))
        

        # first_frame = str(files[0]).split(".")[-2]
        # last_frame = str(files[-1]).split(".")[-2]
        # padding = len(last_frame)

        # return self.media_pool.ImportSequence(
        #     [
        #         {
        #             "FilePath": str(dir / name) + f".%0{padding}d.{ext}",
        #             "StartIndex": int(first_frame),
        #             "EndIndex": int(last_frame),
        #         }
        #     ]
        # )

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


class MediaType(Enum):
    MOVIE = auto()
    SEQUENCE = auto()


class FileType(Enum):
    DPX = MediaType.SEQUENCE
    EXR = MediaType.SEQUENCE
    PNG = MediaType.SEQUENCE
    MOV = MediaType.MOVIE
    MP4 = MediaType.MOVIE
