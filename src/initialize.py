# from datetime import datetime
# import json

# from typing import Optional, Tuple
# from _types import (
#     Project,
#     Timeline,
#     MediaPool,
#     TimelineItem,
#     Folder,
#     MediaPoolItem,
#     MediaStorage,
#     ProjectManager,
#     Resolve,
#     PyRemoteObject,
# )
# from pyresolve import Kernel

# def find_folder_path(
#     root: Folder, media_pool_item: MediaPoolItem
# ) -> Tuple[Folder, list[int], int]:
#     path = []

#     def search_bins(folder: Folder, target_clip: MediaPoolItem, path: list[int]):
#         clips = folder.GetClips()
#         for index, clip in clips.items():
#             if clip.GetMediaId() == target_clip.GetMediaId():
#                 return (folder, path, index)

#         subfolders = folder.GetSubFolders()
#         for index, folder in subfolders.items():
#             if not index:
#                 continue
#             result = search_bins(folder, target_clip, [*path, index])
#             if result:
#                 return result
#         return None

#     result = search_bins(root, media_pool_item, path)

#     if result is None:
#         raise Exception("Could not find bin path")

#     return result


# def encode_media_pool_item_binpath(
#     item: MediaPoolItem, binpath: Tuple[list[int], int], kernel: Kernel
# ) -> bool:
#     """
#     Discover the bin path of the item with recursive search and encode
#     in the metadata of the MediaPoolItem
#     """

#     # folder_path = find_folder_path(kernel.root_folder, item)

#     if binpath is None:
#         return False

#     json_string = json.dumps({"folder_path": binpath[0], "clip_index": binpath[1]})

#     return item.SetThirdPartyMetadata({"path": json_string})


# def retrieve_binpath(
#     item: MediaPoolItem, kernel: Kernel
# ) -> Optional[Tuple[list[int], int]]:
#     json_string = item.GetThirdPartyMetadata("path")

#     if json_string is None:
#         return None

#     if json_string == "":
#         return None
    
#     try:
#         data = json.loads(json_string)

#         data = (data["folder_path"], data["clip_index"])
#         if isinstance(data[0], list) and isinstance(data[1], int):
#             return data
#     except json.JSONDecodeError as e:
#         print(f"Failed to decode JSON: {e}")

#     return None


# def travers_binpath(
#     binpath: Tuple[list[int], int], kernel: Kernel
# ) -> Tuple[Folder, MediaPoolItem]:  # type: ignore
#     root = kernel.root_folder
#     for index in binpath[0]:
#         root = root.GetSubFolders()[index]  # type: ignore

#     clip = root.GetClips()[binpath[1]]  # type: ignore
#     return (root, clip)


# def validate_binpath(
#     item: MediaPoolItem, binpath: Tuple[list[int], int], kernel: Kernel
# ) -> bool:
#     # binpath = access_media_pool_item_binpath(item, kernel)

#     if binpath is None:
#         return False

#     clip = travers_binpath(binpath, kernel)[1]
#     return clip.GetMediaId() == item.GetMediaId()


# def find_clip_bin(item: MediaPoolItem, kernel: Kernel) -> Folder:
#     """
#     First try to find the clip via a cached path,
#     if that fails search for it and cache the path
#     """

#     binpath = retrieve_binpath(item, kernel)

#     if binpath and validate_binpath(item, binpath, kernel):
#         print("successfully located clip via cached path")
#         return travers_binpath(binpath, kernel)[0]

#     if (binpath is None) or (not validate_binpath(item, binpath, kernel)):
#         print("failed to locate clip via cached path, performing search")
#         new_binpath = find_folder_path(kernel.root_folder, item)
#         folder = new_binpath[0]
#         binpath = (new_binpath[1], new_binpath[2])
#         encode_media_pool_item_binpath(item, binpath, kernel)
#         return folder

#     raise Exception(
#         "Failed to find clip's bin"
#     )  # There should be no scenario where we can't find it
