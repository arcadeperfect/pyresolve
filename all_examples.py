#!/usr/bin/env python

"""
    This is a sample slack notification script that is triggered by render job in the deliver page.
    It needs to be placed in the following OS specific directory:
    Mac OS X:   ~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Deliver
    Windows:    %APPDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Deliver\
    Linux:      /opt/resolve/Fusion/Scripts/Deliver/   (or /home/resolve/Fusion/Scripts/Deliver depending on installation)

    This trigger script will receive the following 3 global variables:
    "job" : job id.
    "status" : job status
    "error" : error string(if any)

    This script handles python 2.7 and 3.6. They uses different slack api library version. There is no lua equivalent script because slack does not have official lua api yet.

    These are the slack api guides for different python version:
    For python2.7: https://github.com/slackapi/python-slackclient/tree/v1
    For python3.6: https://github.com/slackapi/python-slackclient

    Before you can run this script,
    for python2.7, you need to install the necessary module for slackclient using the following command: pip install slackclient
    for python3.6, you need to install the necessary module for slackclient using the following command: pip3 install slackclient

    If you encounter ssl error for python3.6 in mac, you have to run "open /Applications/Python\ 3.6/Install\ Certificates.command" in command line

    Please replace the slack_token (i.e. <API_TOKEN_TO_REPLACE>) with API key in order to send notification.
    Please replace the channel_name (i.e. <CHANNEL_NAME_TO_REPLACE>") with the channel that you want to send to.
    A logfile called ScriptRenderLog.txt will be output in the same directory as where this python script is placed in.
"""

import os
import platform
import socket
import sys

# Different versions of python have different official library for slack.
if sys.version_info[0] == 2: #python2.7
    from slackclient import SlackClient
elif sys.version_info[0] == 3: #python3.6
    from slack import WebClient
    from slack.errors import SlackApiError

#slack token and channel name to send notification to.
slack_token = "<API_TOKEN_TO_REPLACE>" #Obtain from the slack api website.
channel_name = "<CHANNEL_NAME_TO_REPLACE>" #eg: #testing_channel

def getJobDetailsBasedOnId(project, jobId):
    jobList = project.GetRenderJobList()
    for jobDetail in jobList:
        if jobDetail["JobId"] == jobId:
            return jobDetail

    return ""

def notifySlack(message):
    if sys.version_info[0] == 2: #python2.7
        sc = SlackClient(slack_token)
        sc.api_call(
          "chat.postMessage",
          channel=channel_name,
          text=message
        )
    elif sys.version_info[0] == 3: #python3.6
        client = WebClient(token=slack_token)
        try:
            response = client.chat_postMessage(
                channel=channel_name,
                text=message
                )
        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            print("Error sending slack message: " + str(e.response['error']))

def main():
    project = resolve.GetProjectManager().GetCurrentProject()
    detailedStatus = project.GetRenderJobStatus(job)
    messageToSend = "Slack Message sent by hostname: {0}, project name: {1}, python version: {2}\n".format(socket.gethostname(), project.GetName(), platform.python_version())
    messageToSend += "Message initiated by: {0}\n".format(os.path.abspath(sys.argv[0]))
    messageToSend += "job id: {0}, job status: {1}, error (if any): \"{2}\"\n". format(job, status, error)
    messageToSend += "Detailed job status: {0}\n".format(str(detailedStatus))
    messageToSend += "Job Details: {0}\n".format(str(getJobDetailsBasedOnId(project, job)))
    notifySlack(messageToSend)

if __name__ == "__main__":
    main()


#!/usr/bin/env python

"""
Example DaVinci Resolve script:
Draw folder and project tree from project manager window.
Example usage: 4_display_project_and_folder_tree.py
"""

from python_get_resolve import GetResolve

def DisplayProjectsWithinFolder( projectManager, folderString = "- ", projectString = "  " ):
    folderString = "  " + folderString
    projectString = "  " + projectString

    projects = sorted(projectManager.GetProjectListInCurrentFolder())
    for projectName in projects:
        print(projectString + projectName)

    folders = sorted(projectManager.GetFolderListInCurrentFolder())
    for folderName in folders:
        print(folderString + folderName)
        if projectManager.OpenFolder(folderName):
            DisplayProjectsWithinFolder(projectManager, folderString, projectString)
            projectManager.GotoParentFolder()
    return

def DisplayProjectTree( resolve ):
    projectManager = resolve.GetProjectManager()
    projectManager.GotoRootFolder()
    print("- Root folder")
    DisplayProjectsWithinFolder(projectManager)
    return

# Get currently open project
resolve = GetResolve()

DisplayProjectTree(resolve)


#!/usr/bin/env python

"""
Sample script to demonstrate following operations to first MediaPool clip in DaVinci Resolve Studio:
1. Add markers
2. Get markers
3. Set customData
4. Delete markers

NOTE: Add one clip (recommended clip duration >= 80 frames) in the MediaPool root bin before running this script.

Example usage: 10_media_pool_marker_operations.py
"""

import os
import sys
from python_get_resolve import GetResolve

resolve = GetResolve()
project = resolve.GetProjectManager().GetCurrentProject()

if not project:
    print("No project is loaded")
    sys.exit()

# Open Media page
resolve.OpenPage("media")

# Get supporting objects
projectManager = resolve.GetProjectManager()
mediaPool = project.GetMediaPool()
rootBin = mediaPool.GetRootFolder()

# Go to root bin
mediaPool.SetCurrentFolder(rootBin)

# Gets clips
clips = rootBin.GetClipList()
if not clips or not clips[0]:
    print("Error: MediaPool root bin doesn't contain any clips, add one clip (recommended clip duration >= 80 frames) and try again!")
    sys.exit()

# Choose first clip in the list
clip = clips[0]

# Get clip frames
framesProperty = clip.GetClipProperty("Frames")
if not framesProperty:
    print("Error: Failed to get clip 'Frames' property !")
    sys.exit()

numFrames = int(framesProperty)

# Add Markers
if (numFrames >= 1):
    isSuccess = clip.AddMarker(1, "Red", "Marker1", "Marker1 at frame 1", 1)
    if isSuccess:
        print("Added marker at FrameId:1")

if (numFrames >= 20):
    isSuccess = clip.AddMarker(20, "Blue", "Marker2", "Marker2 at frame 20", 1, "My Custom Data") # marker with custom data
    if isSuccess:
        print("Added marker at FrameId:20")

if (numFrames >= (50 + 20)):
    isSuccess = clip.AddMarker(50, "Green", "Marker3", "Marker3 at frame 50 (duration 20)", 20) # marker with duration 20 frames
    if isSuccess:
        print("Added marker at FrameId:50")

print("")

# Get all markers for the clip
markers = clip.GetMarkers()
for key, value in markers.items():
    print("Marker at FrameId:%d" % key)
    print(value)

print("")

# Get marker using custom data
markerWithCustomData = clip.GetMarkerByCustomData("My Custom Data")
print("Marker with customData:")
print(markerWithCustomData)

print("")

# Set marker custom data
updatedCustomData = "Updated Custom Data"
isSuccess = clip.UpdateMarkerCustomData(20, updatedCustomData)
if isSuccess:
    print("Updated marker customData at FrameId:20")

print("")

# Get marker custom data
customData = clip.GetMarkerCustomData(20)
print("Marker CustomData at FrameId:20 is:'%s'" % customData)

print("")

# Delete marker using color
isSuccess = clip.DeleteMarkersByColor("Red")
if isSuccess:
    print("Deleted marker with color:'Red'")

# Delete marker using frame number
isSuccess = clip.DeleteMarkerAtFrame(50)
if isSuccess:
    print("Deleted marker at frameNum:50")

# Delete marker using custom data
isSuccess = clip.DeleteMarkerByCustomData(updatedCustomData)
if isSuccess:
    print("Deleted marker with Customdata:'%s'" % updatedCustomData)


#!/usr/bin/env python


"""
Example DaVinci Resolve script:
Based on a given media folder path, this script creates a new project, a default timeline and appends clips into the timeline sorted by name
Example usage: 1_sorted_timeline_from_folder.py project1 24 1920 1080 /Users/username/Movies
"""

from python_get_resolve import GetResolve
import sys

# Inputs:
# - project name
# - project framerate
# - project width, in pixels
# - project height, in pixels
# - path to media
if len(sys.argv) < 6:
    print("input parameters for scripts are [project name] [framerate] [width] [height] [path to media]")
    sys.exit()

projectName = sys.argv[1]
framerate = sys.argv[2]
width = sys.argv[3]
height = sys.argv[4]
mediaPath = sys.argv[5]

# Create project and set parameters:
resolve = GetResolve()
projectManager = resolve.GetProjectManager()
project = projectManager.CreateProject(projectName)

if not project:
    print("Unable to create a project '" + projectName + "'")
    sys.exit()

project.SetSetting("timelineFrameRate", str(framerate))
project.SetSetting("timelineResolutionWidth", str(width))
project.SetSetting("timelineResolutionHeight", str(height))

# Add folder contents to Media Pool:
mediapool = project.GetMediaPool()
rootFolder = mediapool.GetRootFolder()
clips = resolve.GetMediaStorage().AddItemListToMediaPool(mediaPath)

# Create timeline:
timelineName = "Timeline 1"
timeline = mediapool.CreateEmptyTimeline(timelineName)
if not timeline:
    print("Unable to create timeline '" + timelineName + "'")
    sys.exit()

# Sort by name
clips = sorted(clips, key = lambda clip : clip.GetClipProperty("File Name"))

for clip in clips:
    mediapool.AppendToTimeline(clip)

projectManager.SaveProject()

print("'" + projectName + "' has been added")

#!/usr/bin/env python

"""
Example DaVinci Resolve script:
Display current media thumbnail from the color page using open cv plugin
This example is dependent on opencv2 and numpy, which can be installed using: pip install opencv-python numpy
Example usage: 6_get_current_media_thumbnail.py
"""

from python_get_resolve import GetResolve
import array
import base64
import cv2
import numpy as np

# Decode from base64 image string and return cv2 matrix image in BGR format for display
def readb64(base64_string, width, height):
    nparr = np.fromstring(base64.b64decode(base64_string), np.uint8)
    nparr = nparr.reshape(int(height), int(width), 3)
    return cv2.cvtColor(nparr, cv2.COLOR_RGB2BGR)

if __name__ == "__main__":
    resolve = GetResolve()
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()

    timeline = project.GetCurrentTimeline()
    currentMediaThumbnail = timeline.GetCurrentClipThumbnailImage()

    if (currentMediaThumbnail is None) or (len(currentMediaThumbnail) == 0):
        print("There is no current media thumbnail")

    width = currentMediaThumbnail["width"]
    height = currentMediaThumbnail["height"]
    format = currentMediaThumbnail["format"] # Currently we only have RBG 8 bit format

    print("Width of the thumbnail is " + str(width) + ", Height is " + str(height) + ", Format is " + str(format))

    imgstring = currentMediaThumbnail["data"]
    cvimg = readb64(imgstring, width, height)
    cv2.imshow("Current Media Thumbnail", cvimg)
    cv2.waitKey()




#!/usr/bin/env python

"""
Example DaVinci Resolve script:
Adds subclips [frame 0 .. 23] to current timeline for all media pool root folder clips
Example usage: 11_add_subclips_to_mediapool.py project1 24 1920 1080 /Users/username/Movies/sample.mov 0 23
"""

from python_get_resolve import GetResolve
import sys

# Inputs:
# - project name
# - project framerate
# - project width, in pixels
# - project height, in pixels
# - path to media
# - subclip start frame
# - subclip end frame
if len(sys.argv) < 8:
    print("input parameters for scripts are [project name] [framerate] [width] [height] [path to media] [start frame] [end frame]")
    sys.exit()

projectName = sys.argv[1]
framerate = sys.argv[2]
width = sys.argv[3]
height = sys.argv[4]
mediaPath = sys.argv[5]
startFrame = sys.argv[6]
endFrame = sys.argv[7]

# Create project and set parameters:
resolve = GetResolve()
projectManager = resolve.GetProjectManager()
project = projectManager.CreateProject(projectName)

if not project:
    print("Unable to create a project '" + projectName + "'")
    sys.exit()

project.SetSetting("timelineFrameRate", str(framerate))
project.SetSetting("timelineResolutionWidth", str(width))
project.SetSetting("timelineResolutionHeight", str(height))

# Add subclip to Media Pool:
subClip = {
    "media" : mediaPath,
    "startFrame": int(startFrame),
    "endFrame": int(endFrame),
}

resolve.GetMediaStorage().AddItemListToMediaPool([ subClip ])

projectManager.SaveProject()

print("'" + projectName + "' has been added")


#!/usr/bin/env python

"""
Example DaVinci Resolve script:
Exports timeline in different supported formats.
Example usage: 9_export_timeline.py
"""

import os
import sys
from python_get_resolve import GetResolve


def Export(timeline, filePath, exportType, exportSubType=None):
    result = None
    if exportSubType is None:
        result = timeline.Export(filePath, exportType)
    else:
        result = timeline.Export(filePath, exportType, exportSubType)

    if result:
        print("Timeline exported to {0} successfully.".format(filePath))
    else:
        print("Timeline export failed.")


resolve = GetResolve()
project = resolve.GetProjectManager().GetCurrentProject()

if not project:
    print("No project is loaded")
    sys.exit()

aafFilePath = os.path.join(os.path.expanduser("~"), "sampleExp.aaf")
csvFilePath = os.path.join(os.path.expanduser("~"), "sampleExp.csv")

timeline = project.GetCurrentTimeline()
Export(timeline, aafFilePath, resolve.EXPORT_AAF, resolve.EXPORT_AAF_NEW)
Export(timeline, csvFilePath, resolve.EXPORT_TEXT_CSV)


#!/usr/bin/env python


"""
Example DaVinci Resolve script:
Add composition to currently open timeline to timeline clips what do not have any compositions yet
Example usage: 2_compositions_from_timeline_clips.py
"""

from python_get_resolve import GetResolve
import sys

# Get currently open project
resolve = GetResolve()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()

if not project:
    print("No project is loaded")
    sys.exit()

# Get current timeline. If no current timeline try to load it from timeline list
timeline = project.GetCurrentTimeline()
if not timeline:
    if project.GetTimelineCount() > 0:
        timeline = project.GetTimelineByIndex(1)
        project.SetCurrentTimeline(timeline)

if not timeline:
    print("Current project has no timelines")
    sys.exit()

# add compositions for all clips in timeline
timelineVideoTrackCount = timeline.GetTrackCount("video")

for i in range(int(timelineVideoTrackCount)):
    clips = timeline.GetItemListInTrack("video", i + 1)
    for clip in clips:
        if clip.GetFusionCompCount() < 1:
            clip.AddFusionComp()


#!/usr/bin/env python

"""
Example DaVinci Resolve script:
Load a still from DRX file, apply the still to all clips in all timelines. Set render format and codec, add render jobs for all timelines, render to specified path and wait for rendering completion.
Once render is complete, delete all jobs
Example usage: 3_grade_and_render_all_timelines.py /Users/username/Pictures/Still_1.1.1.drx 0 "ProRes Master" /Users/username/Movies/Render mov ProRes422HQ
"""

from python_get_resolve import GetResolve
import sys
import time

def AddTimelineToRender( project, timeline, presetName, targetDirectory, renderFormat, renderCodec ):
    project.SetCurrentTimeline(timeline)
    project.LoadRenderPreset(presetName)

    if not project.SetCurrentRenderFormatAndCodec(renderFormat, renderCodec):
        return False

    project.SetRenderSettings({"SelectAllFrames" : 1, "TargetDir" : targetDirectory})
    return project.AddRenderJob()

def RenderAllTimelines( resolve, presetName, targetDirectory, renderFormat, renderCodec ):
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    if not project:
        return False

    resolve.OpenPage("Deliver")
    timelineCount = project.GetTimelineCount()

    for index in range (0, int(timelineCount)):
        if not AddTimelineToRender(project, project.GetTimelineByIndex(index + 1), presetName, targetDirectory, renderFormat, renderCodec):
            return False
    return project.StartRendering()

def IsRenderingInProgress( resolve ):
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    if not project:
        return False

    return project.IsRenderingInProgress()

def WaitForRenderingCompletion( resolve ):
    while IsRenderingInProgress(resolve):
        time.sleep(1)
    return

def ApplyDRXToAllTimelineClips( timeline, path, gradeMode = 0 ):
    trackCount = timeline.GetTrackCount("video")

    for index in range (1, int(trackCount) + 1):
        clips = timeline.GetItemListInTrack("video", index)
        if not timeline.ApplyGradeFromDRX(path, int(gradeMode), clips):
            return False

    return True

def ApplyDRXToAllTimelines( resolve, path, gradeMode = 0 ):
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    if not project:
        return False
    timelineCount = project.GetTimelineCount()

    for index in range (0, int(timelineCount)):
        timeline = project.GetTimelineByIndex(index + 1)
        project.SetCurrentTimeline( timeline )
        if not ApplyDRXToAllTimelineClips(timeline, path, gradeMode):
            return False
    return True

def DeleteAllRenderJobs( resolve ):
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    project.DeleteAllRenderJobs()
    return

# Inputs:
# - DRX file to import grade still and apply it for clips
# - grade mode (0, 1 or 2)
# - preset name for rendering
# - render path
# - render format
# - render codec
if len(sys.argv) < 7:
    print("input parameters for scripts are [drx file path] [grade mode] [render preset name] [render path] [render format] [render codec]")
    sys.exit()

drxPath = sys.argv[1]
gradeMode = sys.argv[2]
renderPresetName = sys.argv[3]
renderPath = sys.argv[4]
renderFormat = sys.argv[5]
renderCodec = sys.argv[6]

# Get currently open project
resolve = GetResolve()

if not ApplyDRXToAllTimelines(resolve, drxPath, gradeMode):
    print("Unable to apply a still from drx file to all timelines")
    sys.exit()

if not RenderAllTimelines(resolve, renderPresetName, renderPath, renderFormat, renderCodec):
    print("Unable to set all timelines for rendering")
    sys.exit()

WaitForRenderingCompletion(resolve)

DeleteAllRenderJobs(resolve)

print("Rendering is completed.")


#!/usr/bin/env python

"""
Example DaVinci Resolve script:
Adds subclips [frame 0 .. 23] to current timeline for all media pool root folder clips
Example usage: 7_add_subclips_to_timeline.py
"""

from python_get_resolve import GetResolve

if __name__ == "__main__":
    resolve = GetResolve()
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    mediaPool = project.GetMediaPool()
    rootFolder = mediaPool.GetRootFolder()
    clips = rootFolder.GetClipList()

    for clip in clips:
        if clip.GetClipProperty()["Video Codec"] != "":
            subClip = {
                "mediaPoolItem": clip,
                "startFrame": 0,
                "endFrame": 23,
            }

            if mediaPool.AppendToTimeline([ subClip ]):
                print("added subclip (first 24 frames) of \"" + clip.GetName() + "\" to current timeline.")

#!/usr/bin/env python

"""
This file serves to return a DaVinci Resolve object
"""

import sys

def load_source(module_name, file_path):
    if sys.version_info[0] >= 3 and sys.version_info[1] >= 5:
        import importlib.util

        module = None
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec:
            module = importlib.util.module_from_spec(spec)
        if module:
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
        return module
    else:
        import imp
        return imp.load_source(module_name, file_path)


def GetResolve():
    try:
        # The PYTHONPATH needs to be set correctly for this import statement to work.
        # An alternative is to import the DaVinciResolveScript by specifying absolute path (see ExceptionHandler logic)
        import DaVinciResolveScript as bmd
    except ImportError:
        if sys.platform.startswith("darwin"):
            expectedPath = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules/"
        elif sys.platform.startswith("win") or sys.platform.startswith("cygwin"):
            import os
            expectedPath = os.getenv('PROGRAMDATA') + "\\Blackmagic Design\\DaVinci Resolve\\Support\\Developer\\Scripting\\Modules\\"
        elif sys.platform.startswith("linux"):
            expectedPath = "/opt/resolve/Developer/Scripting/Modules/"

        # check if the default path has it...
        print("Unable to find module DaVinciResolveScript from $PYTHONPATH - trying default locations")
        try:
            load_source('DaVinciResolveScript', expectedPath + "DaVinciResolveScript.py")
            import DaVinciResolveScript as bmd
        except Exception as ex:
            # No fallbacks ... report error:
            print("Unable to find module DaVinciResolveScript - please ensure that the module DaVinciResolveScript is discoverable by python")
            print("For a default DaVinci Resolve installation, the module is expected to be located in: " + expectedPath)
            print(ex)
            sys.exit()

    return bmd.scriptapp("Resolve")



#!/usr/bin/env python

"""
Example DaVinci Resolve script:
Display project information: timeline, clips within timelines and media pool structure.
Example usage: 5_get_project_information.py
"""

from python_get_resolve import GetResolve

def DisplayTimelineTrack( timeline, trackType, displayShift ):
    trackCount = timeline.GetTrackCount(trackType)
    for index in range (1, int(trackCount) + 1):
        print(displayShift + "- " + trackType + " " + str(index))
        clips = timeline.GetItemListInTrack(trackType, index)
        for clip in clips:
            print(displayShift + "    " + clip.GetName())
    return

def DisplayTimelineInfo( timeline, displayShift ):
    print(displayShift + "- " + timeline.GetName())
    displayShift = "  " + displayShift
    DisplayTimelineTrack(timeline , "video", displayShift)
    DisplayTimelineTrack(timeline , "audio", displayShift)
    DisplayTimelineTrack(timeline , "subtitle", displayShift)
    return

def DisplayTimelinesInfo( project ):
    print("- Timelines")
    timelineCount = project.GetTimelineCount()

    for index in range (0, int(timelineCount)):
        DisplayTimelineInfo(project.GetTimelineByIndex(index + 1), "  ")
    return

def DisplayFolderInfo( folder, displayShift ):
    print(displayShift + "- " + folder.GetName())
    clips = folder.GetClipList()
    for clip in clips:
        print(displayShift + "  " + clip.GetClipProperty("File Name"))

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

def DisplayProjectInfo( project ):
    print("-----------")
    print("Project '" + project.GetName() +"':")
    print("  Framerate " + str(project.GetSetting("timelineFrameRate")))
    print("  Resolution " + project.GetSetting("timelineResolutionWidth") + "x" + project.GetSetting("timelineResolutionHeight"))

    DisplayTimelinesInfo(project)
    print("")
    DisplayMediaPoolInfo(project)
    return

# Get currently open project
resolve = GetResolve()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()

DisplayProjectInfo(project)
