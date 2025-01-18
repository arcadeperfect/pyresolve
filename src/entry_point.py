from get_resolve import GetResolve
from utils import get_active_clip, find_parent_bin, list_clips_in_bin
from populate_bins import get_shot_paths, create_bins, populate_bins
from mother import SequenceBin, Kernel, MediaType, FileType

import logging
logging.getLogger("pysequitur").setLevel(logging.WARNING)

from pathlib import Path


import time
import os

resolve = GetResolve()
kernel = Kernel(resolve)


# p = Path("P:/projects/ayon/rnd02_ayon/sequences/rndAlexh/rnd010/work/comp/renders/nuke/rendercomp_Main")
# n = "rendercomp_Main"
# ext = "exr"

# kernel.import_sequence(p, n, ext)

# sbin = SequenceBin(
#     "test", 
#     Path("P:/directors/cesar_pelizer/krog81s01_coreHoliday/production/maya/playblast/shots"), 
#     "ANM", 
#     MediaType.MOV, 
#     kernel.root_bin, 
#     kernel
#     )



sbin2 = SequenceBin(
    "test2",
    Path("P:/directors/cesar_pelizer/krog81s01_coreHoliday/production/nuke/shots"),
    "renders",
    FileType.DPX,
    kernel.root_bin,
    kernel
) 

sbin2.create_shot_bins()

for bin in sbin2.shot_bins.values():
    
    
    b = bin.populate_bin(2)
    # print(b)
    

