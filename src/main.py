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
from mother import Kernel

resolve = GetResolve()

kernal = Kernel(resolve)

current = kernal.active_timeline_item

print(current.GetName())

mpi = current.GetMediaPoolItem()

p = mpi.GetName()

print(p)