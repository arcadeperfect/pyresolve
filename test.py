from get_resolve import GetResolve

resolve = GetResolve()
project = resolve.GetProjectManager().GetCurrentProject()
# mediaPool = project.GetMediaPool()

# selected_clips = mediaPool.GetSelectedClips() 

# print(selected_clips)


timeline = project.GetCurrentTimeline()
# current_clip = timeline.GetCurrentVideoItem() 

# print(current_clip)


video_track_count = timeline.GetTrackCount("video")

selected_items = []

# Check each track
for track_index in range(1, int(video_track_count) + 1):
    # Get all items in this track
    items = timeline.GetItemListInTrack("video", track_index)
    
    # Potentially filter based on selection state
    # (Note: Would need to verify if there's a selection state property available)
    for item in items:
        # If we could verify selection state:
        # if item.isSelected():  # Hypothetical - need to verify actual property name
        selected_items.append(item)
        print(item.GetMediaPoolItem().GetClipProperty("File Path"))


# print(selected_items)

# print("\n")

# # for d in dir(selected_items[0]):
# #     print(d)

# mediaPoolItem = selected_items[0].GetMediaPoolItem()

# print(mediaPoolItem.GetClipProperty("File Path"))
