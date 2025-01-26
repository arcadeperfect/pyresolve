from .pyresolve import (
    find_clip_bin,
    Kernel,
    ShotBin,
    SequenceBin,
    SortMode,
    FileType,
    MediaType,
    version_up_track,
    version_down_track,
    version_latest_track,
    version_oldest_track,
    version_up_tracks,
    version_down_tracks,
    version_latest_tracks,
    version_oldest_tracks

)
from .get_resolve import GetResolve
# from .entry_point import *

resolve = GetResolve()
kernel = Kernel(resolve)

i = kernel.active_timeline_item


tli = kernel.active_timeline_item

mpi = kernel.active_media_pool_item


# shot_bin = ShotBin.from_media_pool_item(mpi, kernel)
# shot_bin.version_up(tli, SortMode.VERSIONPARSE)
# shot_bin.version_down(tli, SortMode.VERSIONPARSE)
# shot_bin.version_oldest(tli, SortMode.VERSIONPARSE)
# shot_bin.version_latest(tli, SortMode.VERSIONPARSE)

# version_up_track(1,kernel)
# version_down_track(1,kernel)
# version_latest_track(1, kernel)
# vertion_oldest_track(1, kernel)


# version_oldest_tracks([1,2,3,4], kernel)
# version_latest_tracks([1,2,3,4], kernel)
# version_down_tracks([1,2,3,4], kernel)
version_up_tracks([1,2,3,4], kernel)

# version_latest_track(1, kernel)
