from typing import Optional, List, Dict, Any, Protocol, TypedDict, Union



class PyRemoteObject(Protocol):
    """Base type for all Resolve objects."""

    pass

class Folder(PyRemoteObject):
    """TODO: Add docstring."""

    def ClearTranscription(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def Export(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetClipList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetClips(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetIsFolderStale(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetName(self) -> Any:
        """

        """
        ...

    def GetSubFolderList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetSubFolders(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetUniqueId(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def Print(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def TranscribeAudio(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

class MediaPool(PyRemoteObject):
    """TODO: Add docstring."""

    def AddSubFolder(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def AppendToTimeline(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def AutoSyncAudio(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def CreateEmptyTimeline(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def CreateStereoClip(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def CreateTimelineFromClips(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteClipMattes(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteClips(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteFolders(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteTimelines(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ExportMetadata(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetClipMatteList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetCurrentFolder(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetRootFolder(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetSelectedClips(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetTimelineMatteList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetUniqueId(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ImportFolderFromFile(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ImportMedia(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ImportTimelineFromFile(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def MoveClips(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def MoveFolders(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def Print(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def RefreshFolders(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def RelinkClips(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetCurrentFolder(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetSelectedClip(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def UnlinkClips(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

class MediaPoolItem(PyRemoteObject):
    """TODO: Add docstring."""

    def AddFlag(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def AddMarker(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ClearClipColor(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ClearFlags(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ClearMarkInOut(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ClearTranscription(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteMarkerAtFrame(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteMarkerByCustomData(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteMarkersByColor(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetAudioMapping(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetClipColor(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetClipProperty(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetFlagList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetFlags(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMarkInOut(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMarkerByCustomData(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMarkerCustomData(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMarkers(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMediaId(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMetadata(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetName(self) -> str:
        """        
        File name. Not modifiable. Distinct from the display name returned
        by TimelineItem. Not necessarily unique.
        """
        ...

    def GetThirdPartyMetadata(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetUniqueId(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def LinkProxyMedia(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def Print(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ReplaceClip(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetClipColor(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetClipProperty(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetMarkInOut(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetMetadata(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetThirdPartyMetadata(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def TranscribeAudio(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def UnlinkProxyMedia(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def UpdateMarkerCustomData(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

class MediaStorage(PyRemoteObject):
    """TODO: Add docstring."""

    def AddClipMattesToMediaPool(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def AddItemListToMediaPool(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def AddItemsToMediaPool(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def AddTimelineMattesToMediaPool(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetFileList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetFiles(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMountedVolumeList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMountedVolumes(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetSubFolderList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetSubFolders(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def Print(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def RevealInStorage(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

class Project(PyRemoteObject):
    """TODO: Add docstring."""

    def AddColorGroup(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def AddRenderJob(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteAllRenderJobs(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteColorGroup(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteRenderJob(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteRenderPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ExportCurrentFrameAsStill(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetColorGroupsList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetCurrentRenderFormatAndCodec(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetCurrentRenderMode(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetCurrentTimeline(self) -> Optional[Timeline]:
        """TODO: Add method docstring.

        
        """
        ...

    def GetGallery(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMediaPool(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetName(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetPresetList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetPresets(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetQuickExportRenderPresets(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetRenderCodecs(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetRenderFormats(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetRenderJobList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetRenderJobStatus(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetRenderJobs(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetRenderPresetList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetRenderPresets(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetRenderResolutions(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetSetting(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetTimelineByIndex(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetTimelineCount(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetUniqueId(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def InsertAudioToCurrentTrackAtPlayhead(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def IsRenderingInProgress(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def LoadBurnInPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def LoadRenderPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def Print(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def RefreshLUTList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def RenderWithQuickExport(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SaveAsNewRenderPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetCurrentRenderFormatAndCodec(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetCurrentRenderMode(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetCurrentTimeline(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetName(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetRenderSettings(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetSetting(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def StartRendering(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def StopRendering(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

class ProjectManager(PyRemoteObject):
    """TODO: Add docstring."""

    def ArchiveProject(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def CloseProject(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def CreateCloudProject(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def CreateFolder(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def CreateProject(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteFolder(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteProject(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ExportProject(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetCurrentDatabase(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetCurrentFolder(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetCurrentProject(self) -> Project:
        """TODO: Add method docstring.

        
        """
        ...

    def GetDatabaseList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetFolderListInCurrentFolder(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetFoldersInCurrentFolder(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetProjectLastModifiedTime(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetProjectListInCurrentFolder(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetProjectsInCurrentFolder(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GotoParentFolder(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GotoRootFolder(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ImportCloudProject(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ImportProject(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def LoadCloudProject(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def LoadProject(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def OpenFolder(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def Print(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def RestoreCloudProject(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def RestoreProject(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SaveProject(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetCurrentDatabase(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

class Resolve(PyRemoteObject):
    """Resolve app instance."""

    def DeleteLayoutPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ExportBurnInPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ExportLayoutPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ExportRenderPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def Fusion(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetCurrentPage(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetKeyframeMode(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMediaStorage(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetProductName(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetProjectManager(self) -> ProjectManager:
        """TODO: Add method docstring.

        
        """
        ...

    def GetVersion(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetVersionString(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ImportBurnInPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ImportLayoutPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ImportRenderPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def LoadLayoutPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def OpenPage(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def Print(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def Quit(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SaveLayoutPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetHighPriority(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetKeyframeMode(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def UpdateLayoutPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

class Timeline(PyRemoteObject):
    """TODO: Add docstring."""

    def AddMarker(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def AddTrack(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def AnalyzeDolbyVision(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ClearMarkInOut(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ConvertTimelineToStereo(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def CreateCompoundClip(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def CreateFusionClip(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def CreateSubtitlesFromAudio(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteClips(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteMarkerAtFrame(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteMarkerByCustomData(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteMarkersByColor(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteTrack(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DetectSceneCuts(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DuplicateTimeline(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def Export(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetCurrentClipThumbnailImage(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetCurrentTimecode(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetCurrentVideoItem(self) -> Optional[TimelineItem]:
        """TODO: Add method docstring.

        
        """
        ...

    def GetEndFrame(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetIsTrackEnabled(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetIsTrackLocked(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetItemListInTrack(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetItemsInTrack(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMarkInOut(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMarkerByCustomData(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMarkerCustomData(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMarkers(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMediaPoolItem(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetName(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetNodeGraph(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetSetting(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetStartFrame(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetStartTimecode(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetTrackCount(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetTrackName(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetTrackSubType(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetUniqueId(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GrabAllStills(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GrabStill(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ImportIntoTimeline(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def InsertFusionCompositionIntoTimeline(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def InsertFusionGeneratorIntoTimeline(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def InsertFusionTitleIntoTimeline(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def InsertGeneratorIntoTimeline(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def InsertOFXGeneratorIntoTimeline(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def InsertTitleIntoTimeline(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def Print(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetClipsLinked(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetCurrentTimecode(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetMarkInOut(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetName(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetSetting(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetStartTimecode(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetTrackEnable(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetTrackLock(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetTrackName(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def UpdateMarkerCustomData(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

class TimelineItem(PyRemoteObject):
    """TODO: Add docstring."""

    def AddFlag(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def AddFusionComp(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def AddMarker(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def AddTake(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def AddVersion(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def AssignToColorGroup(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ClearClipColor(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ClearFlags(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def CopyGrades(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def CreateMagicMask(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteFusionCompByName(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteMarkerAtFrame(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteMarkerByCustomData(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteMarkersByColor(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteTakeByIndex(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def DeleteVersionByName(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ExportFusionComp(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ExportLUT(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def FinalizeTake(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetClipColor(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetClipEnabled(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetColorGroup(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetCurrentVersion(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetDuration(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetEnd(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetFlagList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetFlags(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetFusionCompByIndex(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetFusionCompByName(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetFusionCompCount(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetFusionCompNameList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetFusionCompNames(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetIsColorOutputCacheEnabled(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetIsFusionOutputCacheEnabled(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetLUT(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetLeftOffset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetLinkedItems(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMarkerByCustomData(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMarkerCustomData(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMarkers(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetMediaPoolItem(self) -> MediaPoolItem:
        """
        Returns the media pool item of the currently active timeline item, as defined by the playhead (not selection).
        """
        ...

    def GetName(self) -> str:
        """
        Display name. Modifiable, not necessarily unique.

        Returns:
            str
        """
        ...

    def GetNodeGraph(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetNodeLabel(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetNumNodes(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetProperty(self) -> Dict[str, Any]:
        """
        Properties dictionary. Available keys:

        | Property         | Type  |
        | ---------------- | ----- |
        | Pan              | float |
        | Tilt             | float |
        | ZoomX            | float |
        | ZoomY            | float |
        | ZoomGang         | bool  |
        | RotationAngle    | float |
        | AnchorPointX     | float |
        | AnchorPointY     | float |
        | Pitch            | float |
        | Yaw              | float |
        | FlipX            | bool  |
        | FlipY            | bool  |
        | CropLeft         | float |
        | CropRight        | float |
        | CropTop          | float |
        | CropBottom       | float |
        | CropSoftness     | float |
        | CropRetain       | bool  |
        | DynamicZoomEase  | int   |
        | CompositeMode    | int   |
        | Opacity          | float |
        | Distortion       | float |
        | RetimeProcess    | int   |
        | MotionEstimation | int   |
        | Scaling          | int   |
        | ResizeFilter     | int   |
            
        Returns:
            Dict[str, Any]
        """
        ...

    def GetRightOffset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetSelectedTakeIndex(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetSourceAudioChannelMapping(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetSourceEndFrame(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetSourceEndTime(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetSourceStartFrame(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetSourceStartTime(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetStart(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetStereoConvergenceValues(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetStereoLeftFloatingWindowParams(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetStereoRightFloatingWindowParams(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetTakeByIndex(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetTakesCount(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetTrackTypeAndIndex(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetUniqueId(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetVersionNameList(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def GetVersionNames(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def ImportFusionComp(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def LoadBurnInPreset(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def LoadFusionCompByName(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def LoadVersionByName(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def Print(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def RegenerateMagicMask(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def RemoveFromColorGroup(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def RenameFusionCompByName(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def RenameVersionByName(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SelectTakeByIndex(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetCDL(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetClipColor(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetClipEnabled(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetColorOutputCache(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetFusionOutputCache(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetLUT(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SetProperty(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def SmartReframe(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def Stabilize(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def UpdateMarkerCustomData(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...

    def UpdateSidecar(self) -> Any:
        """TODO: Add method docstring.

        
        """
        ...
