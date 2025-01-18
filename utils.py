

def get_active_clip(resolve, project, timeline):

    if not timeline:
        return

    if timeline:
        active_clip = timeline.GetCurrentVideoItem()
        if active_clip:
            return active_clip
        else:
            print("No active clip found")
            return None

def find_parent_bin(media_pool_item, resolve, project):

    # No function in the python api to get the parent bin of a clip, so we have to search

    project = resolve.GetProjectManager().GetCurrentProject()
    media_pool = project.GetMediaPool()
    root_folder = media_pool.GetRootFolder()

    def search_bins(folder, target_clip):

        clips = folder.GetClipList()
        for clip in clips:
            if clip.GetMediaId() == target_clip.GetMediaId():
                return folder

        # Check subfolders
        subfolders = folder.GetSubFolderList()
        for subfolder in subfolders:
            result = search_bins(subfolder, target_clip)
            if result:
                return result
        return None
    
    return search_bins(root_folder, media_pool_item)

def list_clips_in_bin(bin):
    clips = bin.GetClipList()
    for clip in clips:
        print(clip.GetClipProperty("File Name"))