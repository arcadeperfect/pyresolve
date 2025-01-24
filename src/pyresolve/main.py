# from pathlib import Path

# from get_resolve import GetResolve
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
# from pyresolve import Kernel, ShotBin, SortMode, SequenceBin, FileType
# # from initialize import find_clip_bin, retrieve_binpath, encode_media_pool_item_binpath, travers_binpath, validate_binpath

# from datetime import datetime

# import os

# resolve = GetResolve()
# kernel = Kernel(resolve)

# print(kernel.active_media_item.GetName())


# COMPS_ROOT = Path("P:/directors/cesar_pelizer/krog81s01_coreHoliday/production/nuke/shots")
# COMPS_SUBPATH = Path("renders")


# # comps = SequenceBin(
# #     name="comps",
# #     sequence_root_path=COMPS_ROOT,
# #     sub_path=COMPS_SUBPATH,
# #     file_type=FileType.DPX,
# #     parent_bin=kernel.root_folder,
# #     kernel=kernel
# # )

# # comps.create_shot_bins()
# # # comps.populate_shot_bins(-1)

# # timeline = kernel.current_timeline
# # if timeline is None:
# #     exit()

# # t = timeline.AddTrack("video")

# # timeline.AddTrack("video")
# # count = timeline.GetTrackCount("video")
# # p = timeline.SetTrackName("video", count, comps.name)

# # if comps.shot_bins == None:
# #     exit()

# # to_append = []
# # for bin in [comps.shot_bins[key] for key in sorted(comps.shot_bins)]:
# #     n = bin.oldest_clip_in_bin
# #     if n:
# #         print(n)
# #         to_append.append(n)


# # kernel.media_pool.AppendToTimeline(to_append)
    


# # for shot_bin in comps.shot_bins.values():
# #     print(shot_bin.name)

# # for clip in timeline.GetItemListInTrack("video", 1):
# #     shot_bin = ShotBin.from_timeline_item(clip, kernel)
# #     shot_bin.version_up(clip, sort_mode=SortMode.VERSIONPARSE)


