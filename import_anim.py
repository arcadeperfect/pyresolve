from pathlib import Path
import os
import json

from get_resolve import GetResolve

resolve = GetResolve()
project = resolve.GetProjectManager().GetCurrentProject()
media_pool = project.GetMediaPool()
media_storage = resolve.GetMediaStorage()  # Add this line


root_folder = media_pool.GetRootFolder()
anim_path = Path("P:\\directors\\cesar_pelizer\\krog81s01_coreHoliday\\production\\maya\\playblast\\shots")
shots = [p for p in anim_path.iterdir() if p.is_dir()]


# Get list of existing folders
existing_folders = root_folder.GetSubFolderList()

# Delete all existing folders
# if existing_folders:
#     media_pool.DeleteFolders(existing_folders)


# for shot in shots:

#     shot_name = shot.name
#     print(f"{shot_name}")
#     playblast_path = Path(shot) / "ANM"
#     renders = [playblast for playblast in playblast_path.iterdir() 
#                if playblast.is_file()
#                and playblast.suffix == ".mov"]

#     for render in renders:
#         print(f"\t {render}")

# for shot in shots:
#     shot_name = shot.name
#     print(f"Creating bin for {shot_name}")
    
#     # Create bin for this shot
#     shot_bin = media_pool.AddSubFolder(root_folder, shot_name)
    
#     if shot_bin:
#         # Set this as current folder for imports
#         media_pool.SetCurrentFolder(shot_bin)
        
#         playblast_path = Path(shot) / "ANM"
#         renders = [playblast for playblast in playblast_path.iterdir() 
#                   if playblast.is_file()
#                   and playblast.suffix == ".mov"]

#         for render in renders:
#             print(f"\tImporting {render}")
#             # Import the clip into the current bin
#             clips = media_storage.AddItemListToMediaPool(str(render))
#             if clips:
#                 print(f"\tSuccessfully imported {render.name}")
#             else:
#                 print(f"\tFailed to import {render.name}")
#     else:
#         print(f"Failed to create bin for {shot_name}")



# Create a new timeline

timeline_name = "Latest Playblasts"
timeline = media_pool.CreateEmptyTimeline(timeline_name)

bins = root_folder.GetSubFolderList()

for bin in bins:

    clips = bin.GetClipList()

    sorted_clips = sorted(clips, key=lambda clip: clip.GetClipProperty()['File Name'].lower())

    latest_clip = sorted_clips[-1]


    result = media_pool.AppendToTimeline(latest_clip)
    
    if result:
        print(f"Added {latest_clip.GetClipProperty('File Name')} from bin {bin.GetName()}")
    else:
        print(f"Failed to add clip from bin {bin.GetName()}")

