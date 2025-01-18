from get_resolve import GetResolve
from utils import get_active_clip, find_parent_bin, list_clips_in_bin


resolve = GetResolve()
project = resolve.GetProjectManager().GetCurrentProject()
timeline = project.GetCurrentTimeline()





timeline.SetCurrentTimecode(61)
media_pool = project.GetMediaPool()

timeline_item = get_active_clip(resolve, project, timeline)

pool_item = timeline_item.GetMediaPoolItem()

bin = find_parent_bin(pool_item, resolve, project)

clipList =  bin.GetClipList()
clipist = sorted(clipList, key=lambda clip: clip.GetName())
current_index = -1
for x, clip in enumerate(bin.GetClipList()):
    if(clip.GetMediaId() == pool_item.GetMediaId()):
        print(f"{x} of {x}")
        current_index = x

timeline_start = timeline_item.GetStart()
clip_start = timeline_item.GetSourceStartFrame()
clip_end = timeline_item.GetSourceEndFrame()


# print(clipList)

new_item = clipList[current_index - 1]

clipInfo = {
    "mediaPoolItem": new_item,
    "startFrame": clip_start,
    "endFrame": clip_end,
    "mediaType": 1,
    "trackIndex": 1,
    "recordFrame": timeline_start
}
current_tc = timeline.GetCurrentTimecode()
timeline_item.AddTake(new_item, clip_start, clip_end)
take_count = int(timeline_item.GetTakesCount())
print(take_count)
timeline_item.SelectTakeByIndex(2)
timeline_item.FinalizeTake()
# timeline_item.UpdateSidecar()
# timeline.DeleteClips([timeline_item])
# timeline.SetCurrentTimecode(current_tc)


# i = media_pool.AppendToTimeline([clipInfo])
# timeline.SetCurrentTimecode(current_tc)
# print(i)