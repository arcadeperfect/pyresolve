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

from datetime import datetime

resolve = GetResolve()

kernel = Kernel(resolve)

current = kernel.active_timeline_item
mpi = current.GetMediaPoolItem()

# print(current.GetSourceStartFrame())


shotbin = ShotBin.from_media_pool_item(mpi, kernel)

t1 = datetime.now()
newclip = shotbin.query_up(current, SortMode.VERSIONPARSE)
t2 = datetime.now()
print(t2 - t1)


# print(newclip)