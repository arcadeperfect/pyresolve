#!/usr/bin/env python

import os
import glob

# jpg, jpeg, png, exr, dpx ... 
# huggies v01/image search

def DisplayProjectInfo( project ):
   print("-----------")
   print("Project '" + project.GetName() +"':")
   print("  Framerate " + str(project.GetSetting("timelineFrameRate")))
   print("  Resolution " + project.GetSetting("timelineResolutionWidth") + "x" + project.GetSetting("timelineResolutionHeight"))
   
   return

def DisplayFolderInfo( folder, displayShift ):
    print(displayShift + "- " + folder.GetName())
    clips = folder.GetClipList()
    clipList = clips
    for clip in clips:
        #print(displayShift + "  " + clip.GetClipProperty("File Name"))
        #print(displayShift + "  " + clip.GetClipProperty("File Path"))
        #print()
        mediaPoolClipsAndFolders.append([clip, folder])

    displayShift = "  " + displayShift

    folders = folder.GetSubFolderList()
    for folder in folders:
        DisplayFolderInfo(folder, displayShift)
    return
    
def DisplayMediaPoolInfo( project ):
    mediaPool = project.GetMediaPool()
    print("- Media pool")
    DisplayFolderInfo(mediaPool.GetRootFolder(), "  ")
    return


def findMovieFileNeighbors( searchPath, beforeORafter ):
    greaterTimeFileList = []
    lesserTimeFileList = []
    
    # split path and base file name
    dirname, filename = os.path.split(searchPath)
    
    #print(dirname)  
    #print(filename) 
    
    # search for files
    spath = dirname + "\\*_v*"
    list_of_files = glob.glob(spath)
    list_of_files.sort(key=os.path.getmtime)
    
    # get timestamp of current file that is in edit
    timestamp1 = os.path.getmtime(searchPath)
    
    # check for files less than or greater than the timestamp of current file in edit
    for elem in list_of_files:
        timestamp2 = os.path.getmtime(elem)
        if timestamp1 < timestamp2:
            greaterTimeFileList.append(elem)
        elif timestamp1 > timestamp2:
            lesserTimeFileList.append(elem)
            
    print(greaterTimeFileList[0])
    print(lesserTimeFileList[-1])
    print("greater lesser")
    # return the file before or after depending on the string "before" or "after"
    if beforeORafter == "after":
        #print(greaterTimeFileList[0])
        return greaterTimeFileList[0]
    else:
        #print(lesserTimeFileList[-1])
        return lesserTimeFileList[-1]


def findSequenceFileNeighbors( searchPath, beforeORafter ):
    greaterTimeFileList = []
    lesserTimeFileList = []
    folderList = []
    # split path and base file name
    dirname, filename = os.path.split(searchPath)
    
    #print(dirname)  
    #print(filename) 
    
    # get timestamp of current file that is in edit
    timestamp1 = os.path.getmtime(dirname)
    #print(timestamp1)
    
    # split path and base file name
    dirname, filename = os.path.split(searchPath)
    print("clip rootdir " + dirname)
    print("clip name    " + filename)
    print("total frames " + mediaPoolItem.GetClipProperty("Frames"))
    print("start frame  " + mediaPoolItem.GetClipProperty("Start"))
    print("end frame    " + mediaPoolItem.GetClipProperty("End"))
    print("clip format  " + mediaPoolItem.GetClipProperty("Format"))
    
    # get folder of current folder
    rootFolder = os.path.dirname(dirname)
    
    # get list of items in folder
    rootFolderContent = os.listdir(rootFolder)
    
    for folder in rootFolderContent:
        
        if os.path.isdir(rootFolder + "\\" + folder) == True:
            folderList.append(rootFolder + "\\" + folder)
    
    # check for FOLDERS less than or greater than the timestamp of current file in edit
    
    folderList.sort(key=os.path.getmtime)
    
    for elem in folderList:
        timestamp2 = os.path.getmtime(elem)
        if timestamp1 < timestamp2:
            greaterTimeFileList.append(elem)
        elif timestamp1 > timestamp2:
            lesserTimeFileList.append(elem)    

    #print(greaterTimeFileList[0] + " later folder")
    print(lesserTimeFileList[-1] + " earlier folder")
    
    # return the file before or after depending on the string "before" or "after"

    
    #if beforeORafter == "after":
        #print(greaterTimeFileList[0])
        #files = os.listdir(greaterTimeFileList[0])
        #print(os.listdir(greaterTimeFileList[0]))

        #return fileSequenceInfo(greaterTimeFileList[0])
        
    #else:
        #files = os.listdir(lesserTimeFileList[-1])
        
        #return fileSequenceInfo(lesserTimeFileList[-1])
        
 
def fileSequenceInfo( directoryPath ):

    list_of_files = glob.glob(directoryPath + "\\*")
    #print(list_of_files)
    for elem in list_of_files:
        print(elem)
        if elem.endswith(mediaPoolItem.GetClipProperty("Format")) or elem.endswith(mediaPoolItem.GetClipProperty("Format").lower()):
            #print("found " + mediaPoolItem.GetClipProperty("Format"))
            extLen = len(mediaPoolItem.GetClipProperty("Format")) + 1
            fileFrameNumber = os.path.basename(elem)[:-extLen].split(".")[-1]
            #print(fileFrameNumber)
            #print(mediaPoolItem.GetClipProperty("Start"))
            if fileFrameNumber.find(mediaPoolItem.GetClipProperty("Start")) > -1:
                #print(" ==== to start frame ")
                print()
                replaceFile = elem
            
        
        
    return replaceFile
    
    
    
    print(os.path.split(directoryPath)[1])
    fileNameBase = os.path.split(directoryPath)[1]

def getAllClipsOnTimeline(timeline):

    # collection variable
    timeLineItemClips = []

    # get video tracks
    timelineVideoTrackCount = timeline.GetTrackCount("video") 


    # for every clip found on track add to timeLineItemClips
    for i in range(int(timelineVideoTrackCount)):
        clips = timeline.GetItemListInTrack("video", i + 1)
        for clip in clips:
            timeLineItemClips.append(clip)

    # LIST CLIPS IN TIMELINE
    for timelineItem in timeLineItemClips:
        a = timelineItem.GetName()
        print("timeline item name is " + a)
        MPitem = timelineItem.GetMediaPoolItem()
        print("mediapool item path " +  MPitem.GetClipProperty("File Path") )
        print()
        #getClipInfo(MPitem)
 

# --------------- MAIN -------------------


# ----- USER variables -----

beforeORafter = "after"  # value is before or after  ( before means DOWN or earlier, after means UP or later file )

# search for movie files in folder
movieFileExtension = ["mov", "mp4", "avi", "mkv"]
sequenceFileExtension = ["dpx", "exr", "jpg", "jpeg", "png", "tga", "tif", "tiff"]

mediaPoolClipsAndFolders = []

# ----- App variables -----
resolve = app.GetResolve()
fusion = resolve.Fusion()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()

#DisplayProjectInfo(project)
DisplayMediaPoolInfo(project)
mediaStorage = resolve.GetMediaStorage()
mediaPool = project.GetMediaPool()
folderGet = mediaPool.GetRootFolder()


print(" - - - - - ")

# ---------  Get current timeline. If no current timeline try to load it from timeline list
timeline = project.GetCurrentTimeline()
if not timeline:
    if project.GetTimelineCount() > 0:
        timeline = project.GetTimelineByIndex(1)
        project.SetCurrentTimeline(timeline)

if not timeline:
    print("Current project has no timelines")
    sys.exit()


# ----------- get timeline item currently "selected"

timelineItem = timeline.GetCurrentVideoItem() # get current timeline item
mediaPoolItem = timelineItem.GetMediaPoolItem() # get media pool item from timeline item / current clip we want to version
print("current timeline media pool item " + mediaPoolItem.GetClipProperty("File Name"))
searchPath = mediaPoolItem.GetClipProperty("File Path")
# ------------ current timeline clip info
currentTimelineClipName = mediaPoolItem.GetClipProperty("File Name")
currentTimelineClipStartFrame = timelineItem.GetLeftOffset()
currentTimelineClipEndFrame = timelineItem.GetRightOffset()

# ------------- Find what bin for current clip, iterate through list of clips and the folder they live in

currentFolderClipNames = []

print(" HERE IS LIST OF CLIPS AND FOLDERS")
for binItem in mediaPoolClipsAndFolders:
    #print("CLIP NAME = " + binItem[0].GetClipProperty("File Name"))
    #print("FOLDER NAME = " + binItem[1].GetName())
    
    binItemFolder = binItem[1].GetName()
    binItemClip = binItem[0].GetClipProperty("File Name")
    
    
    if binItemClip == currentTimelineClipName:
        print( " +++ match found +++ " + binItemClip + " in BIN >>> " + binItemFolder )
        binItemClipAndFolder = [binItemClip, binItemFolder]
        mediaPool.SetCurrentFolder(binItem[1]) # SET CURRENT BIN !!!!
        currentFolder = binItem[1]
        currentFolderClips = currentFolder.GetClipList()
        for eachClip in currentFolderClips:
            currentFolderClipNames.append([eachClip, eachClip.GetClipProperty("File Name")])
        
    #print("-------")



# ----- FOOTAGE OR MOVIE ------

# split path and base file name
dirname, filename = os.path.split(searchPath)
extension = os.path.splitext(filename)[1][1:]

if extension.lower() in movieFileExtension:
    isMovie=True
    print("found movie file " + extension.lower())
elif extension.lower() in sequenceFileExtension:
    isMovie=False
    print("found sequence " + extension.lower())

print(" ---- ")

if isMovie == True:
    newFootage = findMovieFileNeighbors(searchPath, beforeORafter)
else:
    newFootage = findSequenceFileNeighbors(searchPath, beforeORafter)

print( beforeORafter + " " + newFootage )


# ------ REPLACE FOOTAGE / MOVIE -------

#mediaPoolItem.ReplaceClip("D:\\Projects\\Odd\\BublyBurst2\\Dailies\\BB30_previs_v014.mp4")
#mediaPoolItem.ReplaceClip("D:\\Projects\\Odd\\BublyBurst2\\BublyBurstMaya2\\images\\playblast\\sh0010_previs\\v006\\renderCam_ALT\\jpg\\sh0010_previs_renderCam_ALT_defaultRenderLayer_v006.1001.jpg")
#ppath = "P:\\projects\\huggies\\hugg03_terdAndYuri\\sequence\\exh_exciting_30\\exh_0030\\publish\\render\\rendercomp_Main\\v012\\hugg03_exh_0030_rendercomp_Main_v012.1001.dpx"
#ppath = "P:\\projects\\huggies\\hugg03_terdAndYuri\\sequence\\exh_exciting_30\\exh_0030\\publish\\render\\rendercomp_Main\\v010\\hugg03_exh_0030_rendercomp_Main_v010.1001.dpx"
#mediaPoolItem.ReplaceClip(ppath)
#mediaPoolItem.ReplaceClip(newFootage)
#print(newFootage)


# -------- check if media exist --------
newdirname, newfilename = os.path.split(newFootage)
print(newfilename)
print(currentFolderClipNames)

newClipMedia = []

for currentFolderItem in currentFolderClipNames:
    if newfilename == currentFolderItem[1]:
        print(" FOUND ITEM: " + currentFolderItem[1] )
        print(currentFolderItem)
        newClipMedia.append(currentFolderItem)


# if newClipMedia is empty list then need to import a new clip
if not newClipMedia:

    mediaStorage.AddItemListToMediaPool(newFootage)



    # --------- MAKE updated BIN/folder list ---------------
    print(" - - - - - ")
    updatedFolderClipList = currentFolder.GetClipList()
    updatedFolderClipNames = []

    for jj in updatedFolderClipList:
        updatedFolderClipNames.append([jj, jj.GetClipProperty("File Name")])

    #print(currentFolderClipNames)
    #print(updatedFolderClipNames)


    # ------------ GET the new clip that is new to the list of files in current BIN/folder --------------

      # store as [ mediapool item, File Name ]

    for item1 in updatedFolderClipNames:
        found = False
        for item2 in currentFolderClipNames:
            if item1[1] == item2[1]:
                found = True
        if not found:
            newClipMedia.append(item1)


print(newClipMedia)

# --------------  ADD new clip to timeline as a take and then finalize the take ----------------

#timelineItem.AddTake(mediaPoolItem, startFrame, endFrame) 
timelineItem.AddTake(newClipMedia[0][0], currentTimelineClipStartFrame, currentTimelineClipEndFrame) # add new take
takeCount = int(timelineItem.GetTakesCount()) # should always be 2
timelineItem.SelectTakeByIndex(takeCount) # make new clip current selected take

print()
print("index 1: previous clip info")
print( timelineItem.GetTakeByIndex(1) )
print( timelineItem.GetTakeByIndex(1)["mediaPoolItem"].GetClipProperty("File Name") )

print()
print("index 2: new clip info")
print( timelineItem.GetTakeByIndex(2) )
print( timelineItem.GetTakeByIndex(2)["mediaPoolItem"].GetClipProperty("File Name") )

timelineItem.FinalizeTake() # collapse the take selector to the new clip




# https://gist.github.com/X-Raym/2f2bf453fc481b9cca624d7ca0e19de8

