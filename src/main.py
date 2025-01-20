from get_resolve import GetResolve
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
from mother import Kernel, ShotBin, SortMode
from initialize import access_media_pool_item_binpath, encode_media_pool_item_binpath

from datetime import datetime

resolve = GetResolve()

kernel = Kernel(resolve)

current = kernel.active_timeline_item 
item = current.GetMediaPoolItem() # type: ignore

f = kernel.root_folder

encode_media_pool_item_binpath(item, kernel)

print(access_media_pool_item_binpath(item, kernel))


# p = kernel.find_bin_path(current.GetMediaPoolItem())
# print(p)

# f = kernel.root_folder.GetSubFolders()[2].GetSubFolders()[35].GetName()
# print(f)

# parent = kernel.find_parent_bin(current.GetMediaPoolItem())

# print(parent.GetClips()[1])


# root = kernel.root_folder


# p = root.GetSubFolders()[2].GetName()

# print(p)

# # # print(current.GetSourceStartFrame())


# # shotbin = ShotBin.from_media_pool_item(mpi, kernel)

# # t1 = datetime.now()
# # newclip = shotbin.version_up(current, SortMode.VERSIONPARSE)
# # t2 = datetime.now()
# # print(t2 - t1)


# # # print(newclip)




