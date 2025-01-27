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
    version_oldest_tracks,
    
)
from .get_resolve import GetResolve
# from .entry_point import *
from .entry_point import generate_bins, version_up, version_down, generate_bins_and_assemble, version_oldest_tracks

from pathlib import Path

resolve = GetResolve()
kernel = Kernel(resolve)

i = kernel.active_timeline_item


tli = kernel.active_timeline_item

mpi = kernel.active_media_pool_item



# # my test project
# root = Path(r"P:\projects\ayon\rnd_alexh\Sequences\resolve")
# sub_path= Path(r"publish\render\rendercomp_Main")

# ft = FileType["exr".upper()]
# print(ft)

# sb = SequenceBin(
#     name="comps",
#     sequence_root_path=root,
#     sub_path=sub_path,
#     file_type=ft,
#     parent_bin=kernel.root_folder,
#     kernel=kernel,
# )

# sb.create_folder()
# sb.create_shot_bins()
# sb.populate_shot_bins(4)
# # sb.assemble_timeline(track=1, handle=0)





# current kroger playblasts
root = Path("P:\\directors\\cesar_pelizer\\krog91_omniP13\\production\\maya\\playblast\\shots")
sub_path= Path("ANM")

sb = SequenceBin(
    name="playblasts",
    sequence_root_path=root,
    sub_path=sub_path,
    file_type=FileType.MOV,
    parent_bin=kernel.root_folder,
    kernel=kernel,
)

sb.create_folder()
sb.create_shot_bins()
sb.populate_shot_bins(4)
# sb.assemble_timeline(track=1, handle=0)








# # current kroger renders
# root = Path(r"P:\directors\cesar_pelizer\krog91_omniP13\production\nuke\shots")
# sub_path = Path(r"renders")

# print(root)
# print(root.exists())

# seq_bin = SequenceBin(
#     name="comps",
#     sequence_root_path=root,
#     sub_path=sub_path,
#     file_type=FileType.DPX,
#     parent_bin=kernel.root_folder,
#     kernel=kernel,
# )

# seq_bin.create_folder()
# seq_bin.create_shot_bins()
# seq_bin.populate_shot_bins(-1)
# # seq_bin.assemble_timeline(track=1, handle=0)


