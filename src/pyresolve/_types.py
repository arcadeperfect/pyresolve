from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .typings.DaVinciResolveScript import (
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
else:
    Project = Any
    Timeline = Any
    MediaPool = Any
    TimelineItem = Any
    Folder = Any
    MediaPoolItem = Any
    MediaStorage = Any
    ProjectManager = Any
    Resolve = Any
    PyRemoteObject = Any