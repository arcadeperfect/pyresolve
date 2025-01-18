from pathlib import Path

from mother import Mother
# shot_path = Path("P:\\directors\\cesar_pelizer\\krog81s01_coreHoliday\\production\\maya\\playblast\\shots")
# 
# sub_path = "ANM"
# max_load = 5


def get_shot_paths(shot_path, max_load, sub_path = ""):
    shot_dirs = [p for p in shot_path.iterdir() if p.is_dir()]
    shots = {}
    for shot in shot_dirs:


        shot_name = shot.name
        # print(f"{shot_name}")
        media_path = Path(shot) / sub_path
        if not media_path.is_dir():
            continue
        print(media_path)
        shots[shot_name] = [playblast for playblast in media_path.iterdir() 
                if playblast.is_file()
                and playblast.suffix == ".mov"][-max_load:]

    return shots

def create_bins(parent, names, mother):

    media_pool = mother.project.GetMediaPool()
    existing_bins = [bin.GetName() for bin in parent.GetSubFolderList()]
    bins = []
    for name in names:
        if name in existing_bins:
            print(f"Bin {name} already exists")
            continue
        bin = media_pool.AddSubFolder(parent, name)
        bins.append(bin)

    return bins


def populate_bins(bins, shot_paths, mother):
    media_pool = mother.project.GetMediaPool()

    for bin in bins:
        name = bin.GetName()
        media_pool.SetCurrentFolder(bin)
        for render in shot_paths.get(name, []):
            print(render)
            clips = mother.media_storage.AddItemListToMediaPool(str(render))