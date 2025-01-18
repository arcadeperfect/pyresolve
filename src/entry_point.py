from get_resolve import GetResolve
from utils import get_active_clip, find_parent_bin, list_clips_in_bin
from populate_bins import get_shot_paths, create_bins, populate_bins
from mother import Mother

from pathlib import Path

resolve = GetResolve()
mother = Mother(resolve)



# playblasts_root_path = Path("P:\\directors\\cesar_pelizer\\krog81s01_coreHoliday\\production\\maya\\playblast\\shots")
# playblast_paths = get_shot_paths(playblasts_root_path, 2, "ANM")

# playblast_bin = mother.add_bin("Playblasts")

# bins = mother.add_bins(playblast_paths.keys(), playblast_bin)


# populate_bins(bins, playblast_paths, mother)


comps_root_path = Path("P:\\directors\\cesar_pelizer\\krog81s01_coreHoliday\\production\\nuke\\shots")
comps_paths = get_shot_paths(comps_root_path, 2, "renders")
comp_bin = mother.add_bin("comps")
bins = mother.add_bins(comps_paths.keys(), comp_bin)
# comps_paths 
