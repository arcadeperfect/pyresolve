# from typing import Optional, List, Dict, Any, Protocol, Union

# class PyRemoteObject(Protocol):
#     """Base type for all Resolve objects."""
#     pass

# class Folder(PyRemoteObject):
#     """TODO: Add docstring."""

#     def ClearTranscription(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def Export(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetClipList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetClips(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetIsFolderStale(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetSubFolderList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetSubFolders(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetUniqueId(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def Print(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def TranscribeAudio(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...


# class MediaPool(PyRemoteObject):
#     """TODO: Add docstring."""

#     def AddSubFolder(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def AppendToTimeline(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def AutoSyncAudio(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def CreateEmptyTimeline(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def CreateStereoClip(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def CreateTimelineFromClips(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteClipMattes(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteClips(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteFolders(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteTimelines(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ExportMetadata(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetClipMatteList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetCurrentFolder(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetRootFolder(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetSelectedClips(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetTimelineMatteList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetUniqueId(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ImportFolderFromFile(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ImportMedia(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ImportTimelineFromFile(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def MoveClips(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def MoveFolders(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def Print(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def RefreshFolders(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def RelinkClips(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetCurrentFolder(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetSelectedClip(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def UnlinkClips(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...


# class MediaPoolItem(PyRemoteObject):
#     """TODO: Add docstring."""

#     def AddFlag(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def AddMarker(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ClearClipColor(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ClearFlags(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ClearMarkInOut(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ClearTranscription(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteMarkerAtFrame(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteMarkerByCustomData(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteMarkersByColor(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetAudioMapping(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetClipColor(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetClipProperty(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetFlagList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetFlags(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMarkInOut(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMarkerByCustomData(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMarkerCustomData(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMarkers(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMediaId(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMetadata(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetThirdPartyMetadata(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetUniqueId(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def LinkProxyMedia(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def Print(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ReplaceClip(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetClipColor(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetClipProperty(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetMarkInOut(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetMetadata(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetThirdPartyMetadata(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def TranscribeAudio(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def UnlinkProxyMedia(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def UpdateMarkerCustomData(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...


# class MediaStorage(PyRemoteObject):
#     """TODO: Add docstring."""

#     def AddClipMattesToMediaPool(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def AddItemListToMediaPool(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def AddItemsToMediaPool(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def AddTimelineMattesToMediaPool(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetFileList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetFiles(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMountedVolumeList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMountedVolumes(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetSubFolderList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetSubFolders(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def Print(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def RevealInStorage(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...


# class Project(PyRemoteObject):
#     """TODO: Add docstring."""

#     def AddColorGroup(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def AddRenderJob(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteAllRenderJobs(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteColorGroup(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteRenderJob(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteRenderPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ExportCurrentFrameAsStill(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetColorGroupsList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetCurrentRenderFormatAndCodec(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetCurrentRenderMode(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetCurrentTimeline(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetGallery(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMediaPool(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetPresetList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetPresets(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetQuickExportRenderPresets(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetRenderCodecs(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetRenderFormats(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetRenderJobList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetRenderJobStatus(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetRenderJobs(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetRenderPresetList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetRenderPresets(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetRenderResolutions(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetSetting(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetTimelineByIndex(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetTimelineCount(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetUniqueId(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def InsertAudioToCurrentTrackAtPlayhead(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def IsRenderingInProgress(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def LoadBurnInPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def LoadRenderPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def Print(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def RefreshLUTList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def RenderWithQuickExport(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SaveAsNewRenderPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetCurrentRenderFormatAndCodec(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetCurrentRenderMode(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetCurrentTimeline(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetRenderSettings(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetSetting(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def StartRendering(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def StopRendering(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...


# class ProjectManager(PyRemoteObject):
#     """TODO: Add docstring."""

#     def ArchiveProject(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def CloseProject(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def CreateCloudProject(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def CreateFolder(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def CreateProject(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteFolder(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteProject(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ExportProject(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetCurrentDatabase(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetCurrentFolder(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetCurrentProject(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetDatabaseList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetFolderListInCurrentFolder(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetFoldersInCurrentFolder(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetProjectLastModifiedTime(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetProjectListInCurrentFolder(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetProjectsInCurrentFolder(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GotoParentFolder(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GotoRootFolder(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ImportCloudProject(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ImportProject(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def LoadCloudProject(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def LoadProject(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def OpenFolder(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def Print(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def RestoreCloudProject(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def RestoreProject(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SaveProject(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetCurrentDatabase(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...


# class Resolve(PyRemoteObject):
#     """TODO: Add docstring."""

#     def DeleteLayoutPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ExportBurnInPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ExportLayoutPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ExportRenderPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def Fusion(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetCurrentPage(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetKeyframeMode(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMediaStorage(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetProductName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetProjectManager(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetVersion(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetVersionString(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ImportBurnInPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ImportLayoutPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ImportRenderPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def LoadLayoutPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def OpenPage(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def Print(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def Quit(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SaveLayoutPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetHighPriority(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetKeyframeMode(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def UpdateLayoutPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...


# class Timeline(PyRemoteObject):
#     """TODO: Add docstring."""

#     def AddMarker(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def AddTrack(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def AnalyzeDolbyVision(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ClearMarkInOut(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ConvertTimelineToStereo(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def CreateCompoundClip(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def CreateFusionClip(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def CreateSubtitlesFromAudio(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteClips(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteMarkerAtFrame(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteMarkerByCustomData(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteMarkersByColor(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteTrack(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DetectSceneCuts(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DuplicateTimeline(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def Export(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetCurrentClipThumbnailImage(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetCurrentTimecode(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetCurrentVideoItem(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetEndFrame(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetIsTrackEnabled(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetIsTrackLocked(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetItemListInTrack(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetItemsInTrack(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMarkInOut(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMarkerByCustomData(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMarkerCustomData(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMarkers(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMediaPoolItem(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetNodeGraph(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetSetting(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetStartFrame(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetStartTimecode(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetTrackCount(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetTrackName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetTrackSubType(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetUniqueId(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GrabAllStills(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GrabStill(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ImportIntoTimeline(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def InsertFusionCompositionIntoTimeline(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def InsertFusionGeneratorIntoTimeline(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def InsertFusionTitleIntoTimeline(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def InsertGeneratorIntoTimeline(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def InsertOFXGeneratorIntoTimeline(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def InsertTitleIntoTimeline(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def Print(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetClipsLinked(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetCurrentTimecode(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetMarkInOut(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetSetting(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetStartTimecode(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetTrackEnable(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetTrackLock(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetTrackName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def UpdateMarkerCustomData(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...


# class TimelineItem(PyRemoteObject):
#     """TODO: Add docstring."""

#     def AddFlag(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def AddFusionComp(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def AddMarker(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def AddTake(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def AddVersion(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def AssignToColorGroup(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ClearClipColor(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ClearFlags(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def CopyGrades(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def CreateMagicMask(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteFusionCompByName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteMarkerAtFrame(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteMarkerByCustomData(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteMarkersByColor(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteTakeByIndex(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def DeleteVersionByName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ExportFusionComp(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ExportLUT(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def FinalizeTake(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetClipColor(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetClipEnabled(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetColorGroup(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetCurrentVersion(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetDuration(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetEnd(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetFlagList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetFlags(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetFusionCompByIndex(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetFusionCompByName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetFusionCompCount(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetFusionCompNameList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetFusionCompNames(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetIsColorOutputCacheEnabled(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetIsFusionOutputCacheEnabled(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetLUT(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetLeftOffset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetLinkedItems(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMarkerByCustomData(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMarkerCustomData(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMarkers(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetMediaPoolItem(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetNodeGraph(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetNodeLabel(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetNumNodes(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetProperty(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetRightOffset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetSelectedTakeIndex(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetSourceAudioChannelMapping(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetSourceEndFrame(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetSourceEndTime(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetSourceStartFrame(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetSourceStartTime(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetStart(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetStereoConvergenceValues(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetStereoLeftFloatingWindowParams(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetStereoRightFloatingWindowParams(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetTakeByIndex(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetTakesCount(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetTrackTypeAndIndex(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetUniqueId(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetVersionNameList(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def GetVersionNames(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def ImportFusionComp(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def LoadBurnInPreset(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def LoadFusionCompByName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def LoadVersionByName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def Print(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def RegenerateMagicMask(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def RemoveFromColorGroup(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def RenameFusionCompByName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def RenameVersionByName(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SelectTakeByIndex(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetCDL(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetClipColor(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetClipEnabled(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetColorOutputCache(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetFusionOutputCache(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetLUT(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SetProperty(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def SmartReframe(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def Stabilize(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def UpdateMarkerCustomData(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...

#     def UpdateSidecar(self) -> Any:
#         """TODO: Add method docstring.

#         Returns:
#             Any: TODO: Add return docstring.
#         """
#         ...


