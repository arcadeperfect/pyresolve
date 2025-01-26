from .pyresolve import find_clip_bin, Kernel, ShotBin, SequenceBin, SortMode, version_up_item, version_down_item, FileType, MediaType
from .get_resolve import GetResolve

resolve = GetResolve()
kernel = Kernel(resolve)

i = kernel.active_timeline_item


tli = kernel.active_timeline_item

mpi = kernel.active_media_pool_item


shot_bin = ShotBin.from_timeline_item(tli, kernel)

# shot_bin.version_up(tli, SortMode.VERSIONPARSE)
# shot_bin.version_down(tli, SortMode.VERSIONPARSE)
# shot_bin.version_oldest(tli, SortMode.VERSIONPARSE)
shot_bin.version_latest(tli, SortMode.VERSIONPARSE)




# v = (version_up_item(tli, kernel))