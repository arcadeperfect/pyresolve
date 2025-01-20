import json

from typing import Optional, Tuple
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
from mother import Kernel

# def find_parent_bin(root: Folder, media_pool_item: MediaPoolItem) -> Optional[Folder]:
#     # No function in the python api to get the parent bin of a clip, so we have to search

#     def search_bins(folder: Folder, target_clip: MediaPoolItem):
#         clips = folder.GetClipList()
#         for clip in clips:
#             if clip.GetMediaId() == target_clip.GetMediaId():
#                 return folder

#         # Check subfolders
#         subfolders = folder.GetSubFolderList()
#         for subfolder in subfolders:
#             result = search_bins(subfolder, target_clip)
#             if result:
#                 return result
#         return None

#     return search_bins(root, media_pool_item)


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


def encode_media_pool_item_binpath(item: MediaPoolItem, kernel: Kernel) -> bool:
    """
    Discover the bin path of the item with recursive search and encode
    in the metadata of the MediaPoolItem
    """

    folder_path = find_folder_path(kernel.root_folder, item)

    if folder_path is None:
        return False

    json_string = json.dumps(
        {"folder_path": folder_path[1], "clip_index": folder_path[2]}
    )

    return item.SetThirdPartyMetadata({"path": json_string})


def access_media_pool_item_binpath(
    item: MediaPoolItem, kernel: Kernel
) -> Optional[Tuple[list[int], int]]:
    json_string = item.GetThirdPartyMetadata("path")

    if json_string is None:
        return None

    data = json.loads(json_string)

    data = (data["folder_path"], data["clip_index"])
    if isinstance(data[0], list) and isinstance(data[1], int):
        return data

    return None

def validate_binpath(item: MediaPoolItem, kernel: Kernel) -> bool: