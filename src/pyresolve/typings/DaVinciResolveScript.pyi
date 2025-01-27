from typing import Optional, List, Dict, Any, Protocol, TypedDict, Union, overload



class PyRemoteObject(Protocol):
    """Base type for all Resolve objects."""

    pass

class Folder(PyRemoteObject):
    """Represents a folder in the DaVinci Resolve Media Pool."""
    
    def ClearTranscription(self) -> bool:
        """Clears audio transcription of the MediaPoolItems within the folder and nested folders.
        
        Returns:
            bool: True if successful, False otherwise.
        """
        ...

    def Export(self, filePath: str) -> bool:
        """Returns true if export of DRB folder to filePath is successful, false otherwise.
        
        Args:
            filePath: Path where the DRB folder should be exported.
            
        Returns:
            bool: True if export was successful, False otherwise.
        """
        ...

    def GetClipList(self) -> List[MediaPoolItem]:
        """Returns a list of clips (items) within the folder.
        
        Returns:
            List[MediaPoolItem]: List of MediaPoolItem objects contained in the folder.
        """
        ...

    def GetClips(self) -> dict[int, MediaPoolItem]:
        """Return a dictionary of the contained MediaPoolItems with integers as the keys,
        starting from 1.
        
        Returns:
            dict[int, MediaPoolItem]: Dictionary mapping indices to MediaPoolItems.
        """
        ...

    def GetIsFolderStale(self) -> bool:
        """Returns true if folder is stale in collaboration mode, false otherwise.
        
        Returns:
            bool: True if the folder is stale, False otherwise.
        """
        ...

    def GetName(self) -> str:
        """Returns the media folder name.
        
        Returns:
            str: Name of the folder.
        """
        ...

    def GetSubFolderList(self) -> List["Folder"]:
        """Returns a list of subfolders in the folder.
        
        Returns:
            List[Folder]: List of Folder objects that are subfolders of this folder.
        """
        ...

    def GetSubFolders(self) -> dict[int, "Folder"]:
        """Return a dictionary of the contained Folders with integers as the keys,
        starting from 1.
        
        Returns:
            dict[int, Folder]: Dictionary mapping indices to Folder objects.
        """
        ...

    def GetUniqueId(self) -> str:
        """Returns a unique ID for the media pool folder.
        
        Returns:
            str: Unique identifier for the folder.
        """
        ...

    def Print(self) -> Any:
        """TODO: Add method docstring.
        """
        ...

    def TranscribeAudio(self) -> bool:
        """Transcribes audio of the MediaPoolItems within the folder and nested folders.
        
        Returns:
            bool: True if successful, False otherwise.
        """
        ...


class MediaPool(PyRemoteObject):
    """Represents the Media Pool in DaVinci Resolve, which manages media files and timelines."""

    def AddSubFolder(self, folder: Folder, name: str) -> Folder:
        """Adds new subfolder under specified Folder object with the given name.
        
        Args:
            folder: Parent Folder object to add subfolder to
            name: Name for the new subfolder
            
        Returns:
            Folder: The newly created subfolder
        """
        ...

    # def AppendToTimeline(self, *clips: Union[MediaPoolItem, List[MediaPoolItem], List[Dict]]) -> List["TimelineItem"]:
    #     """Appends specified MediaPoolItem objects in the current timeline.
        
    #     Can be called with:
    #     - Individual MediaPoolItems: clip1, clip2, ...
    #     - List of MediaPoolItems: [clips]
    #     - List of clipInfo dicts: [{"mediaPoolItem": item, "startFrame": float/int, 
    #       "endFrame": float/int, "mediaType": int, "trackIndex": int, "recordFrame": float/int}]
        
    #     Returns:
    #         List[TimelineItem]: List of appended TimelineItems
    #     """
    #     ...

    @overload
    def AppendToTimeline(self, *clips: MediaPoolItem) -> List["TimelineItem"]:
        """
        Appends individual media pool items to the current timeline.

        Args:
            *clips: Variable number of MediaPoolItem objects to append

        Returns:
            List[TimelineItem]: List of appended timeline items

        Example:
            timeline.AppendToTimeline(clip1, clip2, clip3)
        """
        ...

    @overload 
    def AppendToTimeline(self, clips: List[MediaPoolItem]) -> List["TimelineItem"]:
        """
        Appends a list of media pool items to the current timeline.

        Args:
            clips: List of MediaPoolItem objects to append

        Returns:
            List[TimelineItem]: List of appended timeline items

        Example:
            timeline.AppendToTimeline([clip1, clip2, clip3])
        """
        ...

    @overload
    def AppendToTimeline(self, clips: List[Dict[str, Any]]) -> List["TimelineItem"]:
        """
        Appends clips to timeline using clip info dictionaries.

        Args:
            clips: List of dictionaries containing clip information

        Returns:
            List[TimelineItem]: List of appended timeline items

        | Key          | Type          | Required | Description                             |
        | ------------ | ------------- | -------- | --------------------------------------- |
        | mediaPoolItem| MediaPoolItem | Yes      | Media pool item to append              |
        | startFrame   | int/float     | Yes      | Start frame of the clip                |
        | endFrame     | int/float     | Yes      | End frame of the clip                  |
        | mediaType    | int           | No       | 1 for video only, 2 for audio only     |
        | trackIndex   | int           | No       | Index of track to append to            |
        | recordFrame  | int/float     | No       | Frame position to insert clip          |

        Example:
            timeline.AppendToTimeline([{
                "mediaPoolItem": clip1,
                "startFrame": 0,
                "endFrame": 100,
                "mediaType": 1
            }])
        """
        ...

    def AutoSyncAudio(self, clips: List[MediaPoolItem], settings: Dict) -> bool:
        """Syncs audio for specified MediaPoolItems. The list must contain minimum two items.
        
        Args:
            clips: List of MediaPoolItems (at least one video and one audio clip)
            settings: Audio sync settings dictionary
            
        Returns:
            bool: True if successful
        """
        ...

    def CreateEmptyTimeline(self, name: str) -> "Timeline":
        """Adds new timeline with given name.
        
        Args:
            name: Name for the new timeline
            
        Returns:
            Timeline: The newly created timeline
        """
        ...

    def CreateStereoClip(self, leftEyeMediaPoolItem: MediaPoolItem, 
                        rightEyeMediaPoolItem: MediaPoolItem) -> MediaPoolItem:
        """Creates a new 3D stereoscopic media pool entry from two existing media pool items.
        
        Args:
            leftEyeMediaPoolItem: Media pool item for left eye
            rightEyeMediaPoolItem: Media pool item for right eye
            
        Returns:
            MediaPoolItem: The newly created stereo clip
        """
        ...

    def CreateTimelineFromClips(self, name: str, 
                              *clips: Union[MediaPoolItem, List[MediaPoolItem], List[Dict]]) -> "Timeline":
        """Creates new timeline with specified name and appends the specified clips.
        
        Can be called with:
        - name and individual clips: name, clip1, clip2, ...
        - name and list of clips: name, [clips]
        - name and list of clipInfos: name, [{clipInfo}]
        
        Returns:
            Timeline: The newly created timeline
        """
        ...

    def DeleteClipMattes(self, mediaPoolItem: MediaPoolItem, paths: List[str]) -> bool:
        """Delete mattes based on their file paths, for specified MediaPoolItem.
        
        Args:
            mediaPoolItem: Target media pool item
            paths: List of matte file paths to delete
            
        Returns:
            bool: True on success
        """
        ...

    def DeleteClips(self, clips: List[MediaPoolItem]) -> bool:
        """Deletes specified clips or timeline mattes in the media pool.
        
        Args:
            clips: List of clips to delete
            
        Returns:
            bool: True if successful
        """
        ...

    def DeleteFolders(self, subfolders: List[Folder]) -> bool:
        """Deletes specified subfolders in the media pool.
        
        Args:
            subfolders: List of subfolders to delete
            
        Returns:
            bool: True if successful
        """
        ...

    def DeleteTimelines(self, timelines: List["Timeline"]) -> bool:
        """Deletes specified timelines in the media pool.
        
        Args:
            timelines: List of timelines to delete
            
        Returns:
            bool: True if successful
        """
        ...

    def ExportMetadata(self, fileName: str, clips: Optional[List[MediaPoolItem]] = None) -> bool:
        """Exports metadata of specified clips to CSV format.
        
        Args:
            fileName: Path to save the CSV file
            clips: List of clips to export metadata from. If None, uses all clips from media pool
            
        Returns:
            bool: True if successful
        """
        ...

    def GetClipMatteList(self, mediaPoolItem: MediaPoolItem) -> List[str]:
        """Get mattes for specified MediaPoolItem.
        
        Args:
            mediaPoolItem: Media pool item to get mattes from
            
        Returns:
            List[str]: List of paths to the matte files
        """
        ...

    def GetCurrentFolder(self) -> Folder:
        """Returns currently selected Folder.
        
        Returns:
            Folder: Currently selected folder object
        """
        ...

    def GetRootFolder(self) -> Folder:
        """Returns root Folder of Media Pool.
        
        Returns:
            Folder: Root folder object
        """
        ...

    def GetSelectedClips(self) -> List[MediaPoolItem]:
        """Returns the current selected MediaPoolItems.
        
        Returns:
            List[MediaPoolItem]: List of currently selected media pool items
        """
        ...

    def GetTimelineMatteList(self, folder: Folder) -> List[MediaPoolItem]:
        """Get mattes in specified Folder.
        
        Args:
            folder: Folder to get timeline mattes from
            
        Returns:
            List[MediaPoolItem]: List of timeline matte media pool items
        """
        ...

    def GetUniqueId(self) -> str:
        """Returns a unique ID for the media pool.
        
        Returns:
            str: Unique identifier
        """
        ...

    @overload
    def ImportMedia(self, items: List[str]) -> List["MediaPoolItem"]:
        """Imports specified file/folder paths into current Media Pool folder.

        Args:
            items: Array of file/folder paths.

        Returns:
            List of MediaPoolItems created from the import.
        """
        ...

    @overload 
    def ImportMedia(self, items: List[Dict[str, Union[str, int]]]) -> List["MediaPoolItem"]:
        """Imports file paths into current Media Pool folder using clip info specifications.

        Args:
            items: List of clipInfo dictionaries. Each dict can contain:
                  - "FilePath": str (e.g. "file_%03d.dpx")
                  - "StartIndex": int 
                  - "EndIndex": int

        Returns:
            List of MediaPoolItems created from the import.
        """
        ...

    def ImportFolderFromFile(self, filePath: str, sourceClipsPath: str = "") -> bool:
        """Returns true if import from given DRB filePath is successful.
        
        Args:
            filePath: Path to DRB file to import
            sourceClipsPath: Optional path to search for source clips if media is inaccessible
            
        Returns:
            bool: True if successful
        """
        ...

    def ImportTimelineFromFile(self, filePath: str, importOptions: Optional[Dict] = None) -> "Timeline":
        """Creates timeline based on parameters within given file and optional importOptions dict.
        
        Args:
            filePath: Path to timeline file (AAF/EDL/XML/FCPXML/DRT/ADL/OTIO)
            importOptions: Optional dictionary with import settings
            
        Returns:
            Timeline: The newly created timeline
        """
        ...

    def MoveClips(self, clips: List[MediaPoolItem], targetFolder: Folder) -> bool:
        """Moves specified clips to target folder.
        
        Args:
            clips: List of clips to move
            targetFolder: Destination folder
            
        Returns:
            bool: True if successful
        """
        ...

    def MoveFolders(self, folders: List[Folder], targetFolder: Folder) -> bool:
        """Moves specified folders to target folder.
        
        Args:
            folders: List of folders to move
            targetFolder: Destination folder
            
        Returns:
            bool: True if successful
        """
        ...

    def RefreshFolders(self) -> bool:
        """Updates the folders in collaboration mode.
        
        Returns:
            bool: True if successful
        """
        ...

    def RelinkClips(self, clips: List[MediaPoolItem], folderPath: str) -> bool:
        """Update the folder location of specified media pool clips.
        
        Args:
            clips: List of clips to relink
            folderPath: New folder path for the clips
            
        Returns:
            bool: True if successful
        """
        ...

    def SetCurrentFolder(self, folder: Folder) -> bool:
        """Sets current folder by given Folder.
        
        Args:
            folder: Folder to set as current
            
        Returns:
            bool: True if successful
        """
        ...

    def SetSelectedClip(self, clip: MediaPoolItem) -> bool:
        """Sets the selected MediaPoolItem to the given MediaPoolItem.
        
        Args:
            clip: Media pool item to select
            
        Returns:
            bool: True if successful
        """
        ...

    def UnlinkClips(self, clips: List[MediaPoolItem]) -> bool:
        """Unlink specified media pool clips.
        
        Args:
            clips: List of clips to unlink
            
        Returns:
            bool: True if successful
        """
        ...


class MediaPoolItem(PyRemoteObject):
    """Represents a media item in the DaVinci Resolve Media Pool."""

    def AddFlag(self, color: str) -> bool:
        """Adds a flag with given color.
        
        Args:
            color: Flag color to add
            
        Returns:
            bool: True if successful
        """
        ...

    def AddMarker(self, frameId: Union[int, float], color: str, name: str, 
                 note: str, duration: Union[int, float], customData: Optional[str] = None) -> bool:
        """Creates a new marker at given frameId position with given marker information.
        
        Args:
            frameId: Frame position for the marker
            color: Color of the marker
            name: Name of the marker
            note: Note text for the marker
            duration: Duration of the marker
            customData: Optional custom data to attach to the marker
            
        Returns:
            bool: True if successful
        """
        ...

    def ClearClipColor(self) -> bool:
        """Clears the item color.
        
        Returns:
            bool: True if successful
        """
        ...

    def ClearFlags(self, color: str) -> bool:
        """Clear flags of the specified color.
        
        Args:
            color: Color of flags to clear, or "All" to clear all flags
            
        Returns:
            bool: True if successful
        """
        ...

    def ClearMarkInOut(self, markType: str = "all") -> bool:
        """Clears mark in/out points.
        
        Args:
            markType: Type of mark to clear ("video", "audio" or "all")
            
        Returns:
            bool: True if successful
        """
        ...

    def ClearTranscription(self) -> bool:
        """Clears audio transcription of the MediaPoolItem.
        
        Returns:
            bool: True if successful
        """
        ...

    def DeleteMarkerAtFrame(self, frameNum: int) -> bool:
        """Delete marker at frame number from the media pool item.
        
        Args:
            frameNum: Frame number of marker to delete
            
        Returns:
            bool: True if successful
        """
        ...

    def DeleteMarkerByCustomData(self, customData: str) -> bool:
        """Delete first matching marker with specified customData.
        
        Args:
            customData: Custom data string to match
            
        Returns:
            bool: True if successful
        """
        ...

    def DeleteMarkersByColor(self, color: str) -> bool:
        """Delete all markers of the specified color from the media pool item.
        
        Args:
            color: Color of markers to delete, or "All" to delete all markers
            
        Returns:
            bool: True if successful
        """
        ...

    def GetAudioMapping(self) -> str:
        """Returns a string with MediaPoolItem's audio mapping information.
        
        Returns:
            str: JSON formatted string containing audio mapping information
        """
        ...

    def GetClipColor(self) -> str:
        """Returns the item color as a string.
        
        Returns:
            str: Color name
        """
        ...

    # def GetClipProperty(self, propertyName: Optional[str] = None) -> Union[str, float, int, Dict[str, Any]]:
    #     """Returns the property value for the key 'propertyName'.
    #     If no argument is specified, a dict of all clip properties is returned.
        
    #     Args:
    #         propertyName: Optional property name to query
            
    #     Returns:
    #         Union[str, float, int, Dict[str, Any]]: Property value or dictionary of all properties
    #     """
    #     ...
    def GetClipProperty(self, key: str) -> Any:
        """
        Properties dictionary. Available keys:

        | Property                   | Type  |
        | -------------------------- | ----- |
        | Alpha mode                 | str   |
        | Angle                      | str   |
        | Audio Bit Depth            | str   |
        | Audio Ch                   | str   |
        | Audio Codec                | str   |
        | Audio Offset               | str   |
        | Bit Depth                  | str   |
        | Camera #                   | str   |
        | Clip Color                 | str   |
        | Clip Name                  | str   |
        | Cloud Sync                 | str   |
        | Comments                   | str   |
        | Data Level                 | str   |
        | Date Added                 | str   |
        | Date Created               | str   |
        | Date Modified              | str   |
        | Description                | str   |
        | Drop frame                 | str   |
        | Duration                   | str   |
        | Enable Deinterlacing       | str   |
        | End                        | str   |
        | End TC                     | str   |
        | FPS                        | float |
        | Field Dominance            | str   |
        | File Name                  | str   |
        | File Path                  | str   |
        | Flags                      | str   |
        | Format                     | str   |
        | Frames                     | str   |
        | Good Take                  | str   |
        | H-FLIP                     | str   |
        | IDT                        | str   |
        | In                         | str   |
        | Input Color Space          | str   |
        | Input LUT                  | str   |
        | Input Sizing Preset        | str   |
        | Keyword                    | str   |
        | Noise Reduction            | str   |
        | Offline Reference          | str   |
        | Online Status              | str   |
        | Out                        | str   |
        | PAR                        | str   |
        | Proxy                      | str   |
        | Proxy Media Path           | str   |
        | Reel Name                  | str   |
        | Resolution                 | str   |
        | Roll/Card                  | str   |
        | S3D Sync                   | str   |
        | Sample Rate                | str   |
        | Scene                      | str   |
        | Sharpness                  | str   |
        | Shot                       | str   |
        | Slate TC                   | str   |
        | Start                      | str   |
        | Start KeyKode              | str   |
        | Start TC                   | str   |
        | SuperScale Noise Reduction | str   |
        | SuperScale Sharpness       | str   |
        | Synced Audio               | str   |
        | Take                       | str   |
        | Transcription Status       | str   |
        | Type                       | str   |
        | Uploaded From              | str   |
        | Usage                      | str   |
        | V-FLIP                     | str   |
        | Video Codec                | str   |
        | Super Scale                | int   |
            
        """
        ...

    def GetFlagList(self) -> List[str]:
        """Returns a list of flag colors assigned to the item.
        
        Returns:
            List[str]: List of flag colors
        """
        ...

    def GetFlags(self) -> Dict[str, Any]:
        """Undocumented method."""
        ...

    def GetMarkInOut(self) -> Dict[str, Dict[str, int]]:
        """Returns dict of in/out marks set.
        
        Returns:
            Dict containing mark points, e.g.:
            {'video': {'in': 0, 'out': 134}, 'audio': {'in': 0, 'out': 134}}
        """
        ...

    def GetMarkerByCustomData(self, customData: str) -> Dict[str, Any]:
        """Returns marker information for the first matching marker with specified customData.
        
        Args:
            customData: Custom data string to match
            
        Returns:
            Dict[str, Any]: Marker information dictionary
        """
        ...

    def GetMarkerCustomData(self, frameId: Union[int, float]) -> str:
        """Returns customData string for the marker at given frameId position.
        
        Args:
            frameId: Frame position of marker
            
        Returns:
            str: Custom data string
        """
        ...

    def GetMarkers(self) -> Dict[float, Dict[str, Any]]:
        """Returns a dict of all markers and their information.
        
        Returns:
            Dict mapping frame IDs to marker information dictionaries
        """
        ...

    def GetMediaId(self) -> str:
        """Returns the unique ID for the MediaPoolItem.
        
        Returns:
            str: Unique identifier
        """
        ...

    def GetMetadata(self, metadataType: Optional[str] = None) -> Union[str, Dict[str, str]]:
        """Returns the metadata value for the key 'metadataType'.
        If no argument is specified, a dict of all set metadata properties is returned.
        
        Args:
            metadataType: Optional metadata type to query
            
        Returns:
            Union[str, Dict[str, str]]: Metadata value or dictionary of all metadata
        """
        ...

    def GetName(self) -> str:
        """Returns the clip name.
        
        File name. Not modifiable. Distinct from the display name returned
        by TimelineItem. Not necessarily unique.

        
        For image sequences takes the form clip_name.[start_frame]-[end_frame].ext.

        For movies it is just the file name

        Returns:
            str: Name of the clip
        """
        ...

    @overload
    def GetThirdPartyMetadata(self) -> dict[str, str]:
        """
        Return the metadata as a dict
        
        """
        ...
    @overload
    def GetThirdPartyMetadata(self, key) -> str:
        """
        Return the metadata by key
        
        """
        ...

    # def GetThirdPartyMetadata(self, metadataType: Optional[str] = None) -> Union[str, Dict[str, str]]:
    #     """Returns the third party metadata value for the key 'metadataType'.
    #     If no argument is specified, a dict of all set third party metadata properties is returned.
        
    #     Args:
    #         metadataType: Optional metadata type to query
            
    #     Returns:
    #         Union[str, Dict[str, str]]: Metadata value or dictionary of all third party metadata
    #     """
    #     ...

    def GetUniqueId(self) -> str:
        """Returns a unique ID for the media pool item.
        
        Returns:
            str: Unique identifier
        """
        ...

    def LinkProxyMedia(self, proxyMediaFilePath: str) -> bool:
        """Links proxy media located at specified path with the current clip.
        
        Args:
            proxyMediaFilePath: Absolute path to proxy media file
            
        Returns:
            bool: True if successful
        """
        ...

    def Print(self) -> Any:
        """Undocumented method."""
        ...

    def ReplaceClip(self, filePath: str) -> bool:
        """Replaces the underlying asset and metadata of MediaPoolItem with the specified path.
        
        Args:
            filePath: Absolute path to replacement clip
            
        Returns:
            bool: True if successful
        """
        ...

    def SetClipColor(self, colorName: str) -> bool:
        """Sets the item color based on the colorName.
        
        Args:
            colorName: Name of color to set
            
        Returns:
            bool: True if successful
        """
        ...

    def SetClipProperty(self, propertyName: str, propertyValue: Union[str, int, float]) -> bool:
        """Sets the given property to propertyValue.
        
        Args:
            propertyName: Name of property to set
            propertyValue: Value to set
            
        Returns:
            bool: True if successful
        """
        ...

    def SetMarkInOut(self, inPoint: int, outPoint: int, markType: str = "all") -> bool:
        """Sets mark in/out points.
        
        Args:
            inPoint: In point frame number
            outPoint: Out point frame number
            markType: Type of mark to set ("video", "audio" or "all")
            
        Returns:
            bool: True if successful
        """
        ...

    def SetMetadata(self, metadataType: Union[str, Dict[str, str]], 
                   metadataValue: Optional[str] = None) -> bool:
        """Sets the item metadata.
        
        Can be called with:
        - metadataType and metadataValue as separate arguments
        - metadata dictionary as single argument
        
        Returns:
            bool: True if successful
        """
        ...

    def SetThirdPartyMetadata(self, *args) -> bool:
        """Sets/Adds third party metadata.
        
        Can be called with:
        - metadataType and metadataValue as separate arguments
        - metadata dictionary as single argument
        
        Returns:
            bool: True if successful
        """
        ...

    def TranscribeAudio(self) -> bool:
        """Transcribes audio of the MediaPoolItem.
        
        Returns:
            bool: True if successful
        """
        ...

    def UnlinkProxyMedia(self) -> bool:
        """Unlinks any proxy media associated with clip.
        
        Returns:
            bool: True if successful
        """
        ...

    def UpdateMarkerCustomData(self, frameId: Union[int, float], customData: str) -> bool:
        """Updates customData for the marker at given frameId position.
        
        Args:
            frameId: Frame position of marker
            customData: New custom data string
            
        Returns:
            bool: True if successful
        """
        ...

class MediaStorage(PyRemoteObject):
    """Represents the Media Storage browser in DaVinci Resolve, providing access to mounted volumes and media files."""

    def AddClipMattesToMediaPool(self, mediaPoolItem: "MediaPoolItem", paths: List[str], 
                                stereoEye: Optional[str] = None) -> bool:
        """Adds specified media files as mattes for the specified MediaPoolItem.
        
        Args:
            mediaPoolItem: Target media pool item
            paths: List of matte file paths to add
            stereoEye: Optional eye to add matte to for stereo clips ("left" or "right")
            
        Returns:
            bool: True if successful
        """
        ...

    @overload
    def AddItemListToMediaPool(self, *items: str) -> List["MediaPoolItem"]:
        """Adds specified file/folder paths from Media Storage into current Media Pool folder.
        
        Args:
            *items: One or more file/folder paths
            
        Returns:
            List[MediaPoolItem]: List of created MediaPoolItems
        """
        ...

    @overload 
    def AddItemListToMediaPool(self, items: List[str]) -> List["MediaPoolItem"]:
        """Adds specified file/folder paths from Media Storage into current Media Pool folder.
        
        Args:
            items: Array of file/folder paths
            
        Returns:
            List[MediaPoolItem]: List of created MediaPoolItems
        """
        ...

    @overload
    def AddItemListToMediaPool(self, items: List[Dict[str, Union[str, int]]]) -> List["MediaPoolItem"]:
        """Adds list of itemInfos from Media Storage into current Media Pool folder.
        
        Args:
            items: List of dicts containing "media", "startFrame" (int), "endFrame" (int)
            
        Returns:
            List[MediaPoolItem]: List of created MediaPoolItems
        """
        ...

    def AddItemsToMediaPool(self) -> Dict[int, "MediaPoolItem"]:
        """Undocumented method - marked as deprecated in docs but keeping for compatibility."""
        ...

    def AddTimelineMattesToMediaPool(self, paths: List[str]) -> List["MediaPoolItem"]:
        """Adds specified media files as timeline mattes in current media pool folder.
        
        Args:
            paths: List of media file paths to add as timeline mattes
            
        Returns:
            List[MediaPoolItem]: List of created MediaPoolItems
        """
        ...

    def GetFileList(self, folderPath: str) -> List[str]:
        """Returns list of media and file listings in the given absolute folder path.
        Note that media listings may be logically consolidated entries.
        
        Args:
            folderPath: Absolute folder path to list files from
            
        Returns:
            List[str]: List of file paths
        """
        ...

    def GetFiles(self) -> Dict[int, str]:
        """Undocumented method - marked as deprecated in docs but keeping for compatibility."""
        ...

    def GetMountedVolumeList(self) -> List[str]:
        """Returns list of folder paths corresponding to mounted volumes displayed in Resolve's Media Storage.
        
        Returns:
            List[str]: List of mounted volume paths
        """
        ...

    def GetMountedVolumes(self) -> Dict[int, str]:
        """Undocumented method - marked as deprecated in docs but keeping for compatibility."""
        ...

    def GetSubFolderList(self, folderPath: str) -> List[str]:
        """Returns list of folder paths in the given absolute folder path.
        
        Args:
            folderPath: Absolute folder path to list subfolders from
            
        Returns:
            List[str]: List of subfolder paths
        """
        ...

    def GetSubFolders(self) -> Dict[int, str]:
        """Undocumented method - marked as deprecated in docs but keeping for compatibility."""
        ...

    def Print(self) -> Any:
        """Undocumented method."""
        ...

    def RevealInStorage(self, path: str) -> bool:
        """Expands and displays given file/folder path in Resolve's Media Storage.
        
        Args:
            path: Path to file or folder to reveal
            
        Returns:
            bool: True if successful
        """
        ...

class Project(PyRemoteObject):
    """Class representing a DaVinci Resolve project."""

    def AddColorGroup(self, groupName: str) -> ColorGroup:
        """Creates a new ColorGroup. groupName must be a unique string.
        
        Args:
            groupName: Name for the new color group
            
        Returns:
            ColorGroup: The newly created color group
        """
        ...

    def AddRenderJob(self) -> str:
        """Adds a render job based on current render settings to the render queue.
        
        Returns:
            str: Unique job id for the new render job
        """
        ...

    def DeleteAllRenderJobs(self) -> bool:
        """Deletes all render jobs in the queue.
        
        Returns:
            bool: True if successful
        """
        ...

    def DeleteColorGroup(self, colorGroup: ColorGroup) -> bool:
        """Deletes the given color group and sets clips to ungrouped.
        
        Args:
            colorGroup: Color group to delete
            
        Returns:
            bool: True if successful
        """
        ...

    def DeleteRenderJob(self, jobId: str) -> bool:
        """Deletes render job for input job id.
        
        Args:
            jobId: Job ID to delete
            
        Returns:
            bool: True if successful
        """
        ...

    def DeleteRenderPreset(self, presetName: str) -> bool:
        """Delete render preset by provided name.
        
        Args:
            presetName: Name of preset to delete
            
        Returns:
            bool: True if successful
        """
        ...

    def ExportCurrentFrameAsStill(self, filePath: str) -> bool:
        """Exports current frame as still to supplied filePath.
        
        Args:
            filePath: Path to save still (must end in valid export file format)
            
        Returns:
            bool: True if successful
        """
        ...

    def GetColorGroupsList(self) -> List[ColorGroup]:
        """Returns a list of all group objects in the timeline.
        
        Returns:
            List[ColorGroup]: List of color groups
        """
        ...

    def GetCurrentRenderFormatAndCodec(self) -> Dict[str, str]:
        """Returns currently selected format and render codec.
        
        Returns:
            Dict[str, str]: Dictionary with keys 'format' and 'codec'
        """
        ...

    def GetCurrentRenderMode(self) -> int:
        """Returns the render mode.
        
        Returns:
            int: 0 for Individual clips, 1 for Single clip
        """
        ...

    def GetCurrentTimeline(self) -> Optional[Timeline]:
        """Returns the currently loaded timeline.
        
        Returns:
            Optional[Timeline]: Current timeline, if one exists
        """
        ...

    def GetGallery(self) -> Any:
        """Returns the Gallery object.
        
        Returns:
            Gallery: The gallery object
        """
        ...

    def GetMediaPool(self) -> MediaPool:
        """Returns the Media Pool object.
        
        Returns:
            MediaPool: The media pool object
        """
        ...

    def GetName(self) -> str:
        """Returns project name.
        
        Returns:
            str: Name of the project
        """
        ...

    def GetPresetList(self) -> List[Dict[str, Any]]:
        """Returns a list of presets and their information.
        
        Returns:
            List[Dict[str, Any]]: List of presets
        """
        ...

    def GetQuickExportRenderPresets(self) -> List[str]:
        """Returns a list of Quick Export render presets by name.
        
        Returns:
            List[str]: List of preset names
        """
        ...

    def GetRenderCodecs(self, renderFormat: str) -> Dict[str, str]:
        """Returns available codecs for given render format.
        
        Args:
            renderFormat: Render format to get codecs for
            
        Returns:
            Dict[str, str]: Dictionary mapping codec descriptions to codec names
        """
        ...

    def GetRenderFormats(self) -> Dict[str, str]:
        """Returns available render formats.
        
        Returns:
            Dict[str, str]: Dictionary mapping format to file extension
        """
        ...

    def GetRenderJobList(self) -> List[Dict[str, Any]]:
        """Returns a list of render jobs and their information.
        
        Returns:
            List[Dict[str, Any]]: List of render jobs
        """
        ...

    def GetRenderJobStatus(self, jobId: str) -> Dict[str, Any]:
        """Returns job status and completion percentage of the job.
        
        Args:
            jobId: ID of job to check status
            
        Returns:
            Dict[str, Any]: Dictionary with job status info
        """
        ...

    def GetRenderPresetList(self) -> List[Dict[str, Any]]:
        """Returns a list of render presets and their information.
        
        Returns:
            List[Dict[str, Any]]: List of render presets
        """
        ...

    def GetRenderResolutions(self, format: Optional[str] = None, 
                           codec: Optional[str] = None) -> List[Dict[str, int]]:
        """Returns list of resolutions for the given format and codec.
        
        Args:
            format: Optional render format
            codec: Optional render codec
            
        Returns:
            List[Dict[str, int]]: List of resolution dicts with 'Width' and 'Height' keys
        """
        ...

    def GetSetting(self, settingName: str) -> str:
        """Returns value of project setting.
        
        Args:
            settingName: Name of setting to get
            
        Returns:
            str: Setting value
        """
        ...

    def GetTimelineByIndex(self, idx: int) -> Timeline:
        """Returns timeline at the given index.
        
        Args:
            idx: Timeline index (1 <= idx <= project.GetTimelineCount())
            
        Returns:
            Timeline: Timeline at specified index
        """
        ...

    def GetTimelineCount(self) -> int:
        """Returns the number of timelines currently present in the project.
        
        Returns:
            int: Number of timelines
        """
        ...

    def GetUniqueId(self) -> str:
        """Returns a unique ID for the project.
        
        Returns:
            str: Unique ID string
        """
        ...

    def InsertAudioToCurrentTrackAtPlayhead(self, mediaPath: str,
                                          startOffsetInSamples: int,
                                          durationInSamples: int) -> bool:
        """Inserts audio at the playhead on a selected track.
        
        Args:
            mediaPath: Path to media file
            startOffsetInSamples: Start offset in samples
            durationInSamples: Duration in samples
            
        Returns:
            bool: True if successful
        """
        ...

    def IsRenderingInProgress(self) -> bool:
        """Returns True if rendering is in progress.
        
        Returns:
            bool: True if rendering
        """
        ...

    def LoadBurnInPreset(self, presetName: str) -> bool:
        """Loads user defined data burn in preset for project.
        
        Args:
            presetName: Name of preset to load
            
        Returns:
            bool: True if successful
        """
        ...

    def LoadRenderPreset(self, presetName: str) -> bool:
        """Sets a preset as current preset for rendering.
        
        Args:
            presetName: Name of preset to load
            
        Returns:
            bool: True if successful
        """
        ...

    def RefreshLUTList(self) -> bool:
        """Refreshes LUT List.
        
        Returns:
            bool: True if successful
        """
        ...

    def RenderWithQuickExport(self, preset_name: str, param_dict: Dict[str, Any]) -> Dict[str, Any]:
        """Starts a quick export render for the current active timeline.
        
        Args:
            preset_name: Name of preset from GetQuickExportRenderPresets list
            param_dict: Dictionary with render settings keys
            
        Returns:
            Dict[str, Any]: Dictionary with job status and time taken or error string
        """
        ...

    def SaveAsNewRenderPreset(self, presetName: str) -> bool:
        """Creates new render preset by given name if unique.
        
        Args:
            presetName: Name for new preset
            
        Returns:
            bool: True if successful
        """
        ...

    def SetCurrentRenderFormatAndCodec(self, format: str, codec: str) -> bool:
        """Sets given render format and codec as options for rendering.
        
        Args:
            format: Render format to set
            codec: Render codec to set
            
        Returns:
            bool: True if successful
        """
        ...

    def SetCurrentRenderMode(self, renderMode: int) -> bool:
        """Sets the render mode.
        
        Args:
            renderMode: 0 for Individual clips, 1 for Single clip
            
        Returns:
            bool: True if successful
        """
        ...

    def SetCurrentTimeline(self, timeline: Timeline) -> bool:
        """Sets given timeline as current timeline for the project.
        
        Args:
            timeline: Timeline to set as current
            
        Returns:
            bool: True if successful
        """
        ...

    def SetName(self, projectName: str) -> bool:
        """Sets project name if given name is unique.
        
        Args:
            projectName: New name for project
            
        Returns:
            bool: True if successful
        """
        ...

    def SetPreset(self, presetName: str) -> bool:
        """Sets preset by given name into project.
        
        Args:
            presetName: Name of preset to set
            
        Returns:
            bool: True if successful
        """
        ...

    def SetRenderSettings(self, settings: Dict[str, Any]) -> bool:
        """Sets given settings for rendering.
        
        Args:
            settings: Dictionary of render settings
            
        Returns:
            bool: True if successful
        """
        ...

    def SetSetting(self, settingName: str, settingValue: str) -> bool:
        """Sets the project setting to the value.
        
        Args:
            settingName: Name of setting to set
            settingValue: Value to set
            
        Returns:
            bool: True if successful
        """
        ...

    def StartRendering(self, *args: Union[str, List[str], bool]) -> bool:
        """Starts rendering jobs. Can be called as:
        - StartRendering(jobId1, jobId2, ...) with individual job IDs
        - StartRendering([jobIds], isInteractiveMode=False) with list of job IDs
        - StartRendering(isInteractiveMode=False) to render all queued jobs
        
        Args:
            *args: Job IDs and optional interactive mode flag
            
        Returns:
            bool: True if successful
        
        Note: isInteractiveMode enables error feedback in the UI during rendering
        """
        ...

    def StopRendering(self) -> None:
        """Stops any current render processes."""
        ...

class ProjectManager(PyRemoteObject):
   """Manages DaVinci Resolve projects, databases, and project folders."""
   
   def ArchiveProject(self, projectName: str, filePath: str, 
                     isArchiveSrcMedia: bool = True,
                     isArchiveRenderCache: bool = True, 
                     isArchiveProxyMedia: bool = False) -> bool:
       """Archives project to provided file path with the specified configuration.
       
       Args:
           projectName: Name of project to archive
           filePath: Path to save archive 
           isArchiveSrcMedia: Whether to archive source media. Defaults to True
           isArchiveRenderCache: Whether to archive render cache. Defaults to True
           isArchiveProxyMedia: Whether to archive proxy media. Defaults to False
           
       Returns:
           bool: True if successful
       """
       ...

   def CloseProject(self, project: Project) -> bool:
       """Closes the specified project without saving.
       
       Args:
           project: Project to close
           
       Returns:
           bool: True if successful
       """
       ...

   def CreateCloudProject(self, cloudSettings: Dict[str, Any]) -> Project:
       """Creates and returns a cloud project.
       
       Args:
           cloudSettings: Dictionary with cloud project settings
           
       Returns:
           Project: The newly created cloud project
       """
       ...

   def CreateFolder(self, folderName: str) -> bool:
       """Creates a folder if folderName is unique.
       
       Args:
           folderName: Name for new folder
           
       Returns:
           bool: True if successful
       """
       ...

   def CreateProject(self, projectName: str) -> Project:
       """Creates and returns a project if projectName is unique.
       
       Args:
           projectName: Name for new project
           
       Returns:
           Project: The newly created project, None if name not unique
       """
       ...

   def DeleteFolder(self, folderName: str) -> bool:
       """Deletes the specified folder if it exists.
       
       Args:
           folderName: Name of folder to delete
           
       Returns:
           bool: True if successful
       """
       ...

   def DeleteProject(self, projectName: str) -> bool:
       """Delete project in the current folder if not currently loaded.
       
       Args:
           projectName: Name of project to delete
           
       Returns:
           bool: True if successful
       """
       ...

   def ExportProject(self, projectName: str, filePath: str, 
                    withStillsAndLUTs: bool = True) -> bool:
       """Exports project to provided file path.
       
       Args:
           projectName: Name of project to export
           filePath: Path to export to
           withStillsAndLUTs: Whether to include stills and LUTs. Defaults to True
           
       Returns:
           bool: True if successful
       """
       ...

   def GetCurrentDatabase(self) -> Dict[str, str]:
       """Returns info about current database connection.
       
       Returns:
           Dict with keys 'DbType', 'DbName' and optional 'IpAddress'
       """
       ...

   def GetCurrentFolder(self) -> str:
       """Returns the current folder name.
       
       Returns:
           str: Current folder name
       """
       ...

   def GetCurrentProject(self) -> Project:
       """Returns the currently loaded Resolve project.
       
       Returns:
           Project: Currently loaded project
       """
       ...

   def GetDatabaseList(self) -> List[Dict[str, str]]:
       """Returns list of all databases added to Resolve.
       
       Returns:
           List of dicts with keys 'DbType', 'DbName' and optional 'IpAddress'
       """
       ...

   def GetFolderListInCurrentFolder(self) -> List[str]:
       """Returns a list of folder names in current folder.
       
       Returns:
           List[str]: List of folder names
       """
       ...

   def GetFoldersInCurrentFolder(self) -> Dict[int, str]:
       """Undocumented method - marked as deprecated in docs but keeping for compatibility."""
       ...

   def GetProjectLastModifiedTime(self) -> Any:
       """Undocumented method."""
       ...

   def GetProjectListInCurrentFolder(self) -> List[str]:
       """Returns a list of project names in current folder.
       
       Returns:
           List[str]: List of project names
       """
       ...

   def GetProjectsInCurrentFolder(self) -> Dict[str, Any]:
       """Undocumented method - marked as deprecated in docs but keeping for compatibility."""
       ...

   def GotoParentFolder(self) -> bool:
       """Opens parent folder of current folder in database if current folder has parent.
       
       Returns:
           bool: True if successful
       """
       ...

   def GotoRootFolder(self) -> bool:
       """Opens root folder in database.
       
       Returns:
           bool: True if successful
       """
       ...

   def ImportCloudProject(self, filePath: str, cloudSettings: Dict[str, Any]) -> bool:
       """Imports a cloud project from the specified file path.
       
       Args:
           filePath: Path of file to import
           cloudSettings: Dictionary with cloud settings

       Returns:
           bool: True if successful
       """
       ...

   def ImportProject(self, filePath: str, projectName: Optional[str] = None) -> bool:
       """Imports a project from the file path provided.
       
       Args:
           filePath: Path to project file
           projectName: Optional name for imported project
           
       Returns:
           bool: True if successful
       """
       ...

   def LoadCloudProject(self, cloudSettings: Dict[str, Any]) -> Project:
       """Loads and returns a cloud project with the specified settings.
       
       Args:
           cloudSettings: Dictionary with cloud project settings
           
       Returns:
           Project: The loaded cloud project, None if not found
       """
       ...

   def LoadProject(self, projectName: str) -> Project:
       """Loads and returns the project with the given name.
       
       Args:
           projectName: Name of project to load
           
       Returns:
           Project: The loaded project if found, None if not found
       """
       ...

   def OpenFolder(self, folderName: str) -> bool:
       """Opens folder under given name.
       
       Args:
           folderName: Name of folder to open
           
       Returns:
           bool: True if successful
       """
       ...

   def Print(self) -> Any:
       """Undocumented method."""
       ...

   def RestoreCloudProject(self, folderPath: str, cloudSettings: Dict[str, Any]) -> bool:
       """Restores a cloud project from the specified folder.
       
       Args:
           folderPath: Path of folder to restore from
           cloudSettings: Dictionary with cloud settings
           
       Returns:
           bool: True if successful
       """
       ...

   def RestoreProject(self, filePath: str, projectName: Optional[str] = None) -> bool:
       """Restores a project from the file path provided.
       
       Args:
           filePath: Path to restore from
           projectName: Optional name for restored project
           
       Returns:
           bool: True if successful
       """
       ...

   def SaveProject(self) -> bool:
       """Saves the currently loaded project with its own name.
       
       Returns:
           bool: True if successful
       """
       ...

   def SetCurrentDatabase(self, dbInfo: Dict[str, str]) -> bool:
       """Switches current database connection and closes any open project.
       
       Args:
           dbInfo: Dictionary with keys:
                  - 'DbType': 'Disk' or 'PostgreSQL' 
                  - 'DbName': database name
                  - 'IpAddress': IP address (optional, defaults to '127.0.0.1')
           
       Returns:
           bool: True if successful
       """
       ...
       

class Resolve(PyRemoteObject):
   """Main DaVinci Resolve application instance - the fundamental starting point for scripting."""

   def DeleteLayoutPreset(self, presetName: str) -> bool:
       """Deletes preset named 'presetName'.
       
       Args:
           presetName: Name of preset to delete
           
       Returns:
           bool: True if successful
       """
       ...

   def ExportBurnInPreset(self, presetName: str, exportPath: str) -> bool:
       """Export a data burn in preset if presetName exists.
       
       Args:
           presetName: Name of preset to export
           exportPath: Path to export to
           
       Returns:
           bool: True if successful
       """
       ...

   def ExportLayoutPreset(self, presetName: str, presetFilePath: str) -> bool:
       """Exports preset named 'presetName' to path 'presetFilePath'.
       
       Args:
           presetName: Name of preset to export
           presetFilePath: Path to export to
           
       Returns:
           bool: True if successful
       """
       ...

   def ExportRenderPreset(self, presetName: str, exportPath: str) -> bool:
       """Export a preset to a given path if presetName exists.
       
       Args:
           presetName: Name of preset to export
           exportPath: Path to export to
           
       Returns:
           bool: True if successful
       """
       ...

   def Fusion(self) -> Graph:
       """Returns the Fusion object. Starting point for Fusion scripts.
       
       Returns:
           Fusion: The Fusion object
       """
       ...

   def GetCurrentPage(self) -> Optional[str]:
       """Returns the page currently displayed in the main window.
       
       Returns:
           str: One of ("media", "cut", "edit", "fusion", "color", "fairlight", "deliver", None)
       """
       ...

   def GetKeyframeMode(self) -> int:
       """Returns the currently set keyframe mode.
       
       Returns:
           int: 0=KEYFRAME_MODE_ALL, 1=KEYFRAME_MODE_COLOR, 2=KEYFRAME_MODE_SIZING
       """
       ...

   def GetMediaStorage(self) -> MediaStorage:
       """Returns the media storage object to query and act on media locations.
       
       Returns:
           MediaStorage: The media storage object
       """
       ...

   def GetProductName(self) -> str:
       """Returns product name.
       
       Returns:
           str: Product name
       """
       ...

   def GetProjectManager(self) -> ProjectManager:
       """Returns the project manager object for currently open database.
       
       Returns:
           ProjectManager: The project manager object
       """
       ...

   def GetVersion(self) -> List[Union[int, str]]:
       """Returns list of product version fields.
       
       Returns:
           List containing [major, minor, patch, build, suffix]
       """
       ...

   def GetVersionString(self) -> str:
       """Returns product version in "major.minor.patch[suffix].build" format.
       
       Returns:
           str: Version string
       """
       ...

   def ImportBurnInPreset(self, presetPath: str) -> bool:
       """Import a data burn in preset from a given presetPath.
       
       Args:
           presetPath: Path to preset file
           
       Returns:
           bool: True if successful
       """
       ...

   def ImportLayoutPreset(self, presetFilePath: str, presetName: Optional[str] = None) -> bool:
       """Imports preset from path 'presetFilePath'.
       
       Args:
           presetFilePath: Path to preset file
           presetName: Optional name for imported preset
           
       Returns:
           bool: True if successful
       """
       ...

   def ImportRenderPreset(self, presetPath: str) -> bool:
       """Import a preset and set it as current preset for rendering.
       
       Args:
           presetPath: Path to preset file
           
       Returns:
           bool: True if successful
       """
       ...

   def LoadLayoutPreset(self, presetName: str) -> bool:
       """Loads UI layout from saved preset named 'presetName'.
       
       Args:
           presetName: Name of preset to load
           
       Returns:
           bool: True if successful
       """
       ...

   def OpenPage(self, pageName: str) -> bool:
       """Switches to indicated page in DaVinci Resolve.
       
       Args:
           pageName: One of ("media", "cut", "edit", "fusion", "color", "fairlight", "deliver")
           
       Returns:
           bool: True if successful
       """
       ...

   def Print(self) -> Any:
       """Undocumented method."""
       ...

   def Quit(self) -> None:
       """Quits the Resolve App."""
       ...

   def SaveLayoutPreset(self, presetName: str) -> bool:
       """Saves current UI layout as a preset named 'presetName'.
       
       Args:
           presetName: Name for the saved preset
           
       Returns:
           bool: True if successful
       """
       ...

   def SetHighPriority(self) -> Any:
       """Undocumented method."""
       ...

   def SetKeyframeMode(self, keyframeMode: int) -> bool:
       """Sets the keyframe mode.
       
       Args:
           keyframeMode: 0=KEYFRAME_MODE_ALL, 1=KEYFRAME_MODE_COLOR, 2=KEYFRAME_MODE_SIZING
           
       Returns:
           bool: True when successfully set
       """
       ...

   def UpdateLayoutPreset(self, presetName: str) -> bool:
       """Overwrites preset named 'presetName' with current UI layout.
       
       Args:
           presetName: Name of preset to update
           
       Returns:
           bool: True if successful
       """
       ...

class Timeline(PyRemoteObject):
    """Class representing a Timeline in DaVinci Resolve."""

    def AddMarker(self, frameId: int, color: str, name: str, note: str, duration: float, customData: Optional[str] = None) -> bool:
        """Creates a new marker at given frameId position with given marker information.

        Args:
            frameId (int): Frame position for the marker
            color (str): Color of the marker
            name (str): Name of the marker
            note (str): Note text for the marker
            duration (float): Duration of the marker
            customData (Optional[str], optional): Custom data to attach to the marker. Defaults to None.

        Returns:
            bool: True if successful
        """
        ...

    def AddTrack(self, trackType: str) -> bool:
        """Add a track

        Args:
            trackType (str): The type of track to add: "video", "audio", "subtitle"

        Returns:
            bool: True if successful
        """
        ...

    def AnalyzeDolbyVision(self, timelineItems: Optional[list] = None, analysisType: Optional[int] = None) -> bool:
        """Analyzes Dolby Vision on clips present on the timeline.

        Args:
            timelineItems (Optional[list], optional): List of timeline items. If empty, analysis performed on all items. Defaults to None.
            analysisType (Optional[int], optional): Analysis type. Use resolve.DLB_BLEND_SHOTS for blend setting. Defaults to None.

        Returns:
            bool: True if analysis start is successful
        """
        ...

    def ClearMarkInOut(self, type: str = "all") -> bool:
        """Clears mark in/out points.

        Args:
            type (str, optional): Type of marks to clear - "video", "audio" or "all". Defaults to "all".

        Returns:
            bool: True if successful
        """
        ...

    def ConvertTimelineToStereo(self) -> bool:
        """Converts timeline to stereo.

        Returns:
            bool: True if successful
        """
        ...

    def CreateCompoundClip(self, timelineItems: list, clipInfo: Optional[dict] = None) -> TimelineItem:
        """Creates a compound clip of input timeline items.

        Args:
            timelineItems (list): List of timeline items to include
            clipInfo (Optional[dict], optional): Optional clip info map with keys "startTimecode" and "name". Defaults to None.

        Returns:
            TimelineItem: The created timeline item
        """
        ...

    def CreateFusionClip(self, timelineItems: list) -> TimelineItem:
        """Creates a Fusion clip of input timeline items.

        Args:
            timelineItems (list): List of timeline items to include

        Returns:
            TimelineItem: The created timeline item
        """
        ...

    def CreateSubtitlesFromAudio(self, autoCaptionSettings: Optional[dict] = None) -> bool:
        """Creates subtitles from audio for the timeline.

        Args:
            autoCaptionSettings (Optional[dict], optional): Dictionary of auto caption settings. Defaults to None.

        Returns:
            bool: True if successful
        """
        ...

    def DeleteClips(self, timelineItems: list, rippleDelete: bool = False) -> bool:
        """Deletes specified TimelineItems from the timeline.

        Args:
            timelineItems (list): List of timeline items to delete
            rippleDelete (bool, optional): Whether to perform ripple delete. Defaults to False.

        Returns:
            bool: True if successful
        """
        ...

    def DeleteMarkerAtFrame(self, frameNum: int) -> bool:
        """Deletes the timeline marker at the given frame number.

        Args:
            frameNum (int): Frame number of marker to delete

        Returns:
            bool: True if successful
        """
        ...

    def DeleteMarkerByCustomData(self, customData: str) -> bool:
        """Delete first matching marker with specified customData.

        Args:
            customData (str): Custom data to match

        Returns:
            bool: True if successful
        """
        ...

    def DeleteMarkersByColor(self, color: str) -> bool:
        """Deletes all timeline markers of the specified color.

        Args:
            color (str): Color of markers to delete, or "All" to delete all markers

        Returns:
            bool: True if successful
        """
        ...

    def DeleteTrack(self, trackType: str, trackIndex: int) -> bool:
        """Deletes track of specified type and index.

        Args:
            trackType (str): Type of track to delete ("video", "subtitle", "audio")
            trackIndex (int): Index of track to delete (1 <= trackIndex <= GetTrackCount(trackType))

        Returns:
            bool: True if successful
        """
        ...

    def DetectSceneCuts(self) -> bool:
        """Detects and makes scene cuts along the timeline.

        Returns:
            bool: True if successful
        """
        ...

    def DuplicateTimeline(self, timelineName: Optional[str] = None) -> Timeline:
        """Duplicates the timeline.

        Args:
            timelineName (Optional[str], optional): Name for the duplicated timeline. Defaults to None.

        Returns:
            Timeline: The created timeline if successful
        """
        ...

    def Export(self, fileName: str, exportType: int, exportSubtype: Optional[int] = None) -> bool:
        """Exports timeline to specified format.

        Args:
            fileName (str): Output file path
            exportType (int): Export format type constant
            exportSubtype (Optional[int], optional): Export format subtype constant. Defaults to None.

        Returns:
            bool: True if successful
        """
        ...

    def GetCurrentClipThumbnailImage(self) -> dict:
        """Returns thumbnail data for current media in the Color Page.

        Returns:
            dict: Dictionary with keys "width", "height", "format" and "data" containing thumbnail image data
        """
        ...

    def GetCurrentTimecode(self) -> str:
        """Returns timecode for the current playhead position.

        Returns:
            str: Timecode string
        """
        ...

    def GetCurrentVideoItem(self) -> Optional[TimelineItem]:
        """Returns the current video timeline item.
        
        Returns:
            Optional[TimelineItem]: Current video timeline item if one exists
        """
        ...

    def GetEndFrame(self) -> int:
        """Returns the frame number at the end of timeline.
        
        Returns:
            int: End frame number
        """
        ...

    def GetIsTrackEnabled(self, trackType: str, trackIndex: int) -> bool:
        """Returns whether track is enabled.

        Args:
            trackType (str): Type of track ("audio", "video", "subtitle")
            trackIndex (int): Index of track (1 <= trackIndex <= GetTrackCount(trackType))

        Returns:
            bool: True if track is enabled
        """
        ...

    def GetIsTrackLocked(self, trackType: str, trackIndex: int) -> bool:
        """Returns whether track is locked.

        Args:
            trackType (str): Type of track ("audio", "video", "subtitle")
            trackIndex (int): Index of track (1 <= trackIndex <= GetTrackCount(trackType))

        Returns:
            bool: True if track is locked
        """
        ...

    def GetItemListInTrack(self, trackType: str, index: int) -> Optional[list[TimelineItem]]:
        """Gets list of timeline items in specified track.

        Args:
            trackType (str): Type of track ("video" or "audio")
            index (int): Index of track, starting from 1

        Returns:
            Optional[list[TimelineItem]]: List of TimelineItems in specified track
        """
        ...

    def GetItemsInTrack(self, trackType: str, index: int) -> dict[int, TimelineItem]:
        """Gets dict of timeline items in specified track.

        Args:
            trackType (str): Type of track ("video" or "audio")
            index (int): Index of track, starting from 1
            
        Returns:
            dict[int, TimelineItem]: Dict of TimelineItems with integers as keys, starting from 1
        """
        ...

    def GetMarkInOut(self) -> dict:
        """Returns dict of in/out marks.

        Returns:
            dict: Dictionary with mark info, e.g. {'video': {'in': 0, 'out': 134}, 'audio': {'in': 0, 'out': 134}}
        """
        ...

    def GetMarkerByCustomData(self, customData: str) -> dict:
        """Returns marker info for first matching marker with specified customData.

        Args:
            customData (str): Custom data to match

        Returns:
            dict: Marker information dictionary
        """
        ...

    def GetMarkerCustomData(self, frameId: int) -> str:
        """Returns custom data string for marker at given frame.

        Args:
            frameId (int): Frame ID of marker

        Returns:
            str: Custom data string
        """
        ...

    def GetMarkers(self) -> dict:
        """Returns all timeline markers and their information.

        Returns:
            dict: Dictionary mapping frame IDs to marker information dictionaries
        """
        ...

    def GetMediaPoolItem(self) -> MediaPoolItem:
        """Returns the media pool item corresponding to the timeline.

        Returns:
            MediaPoolItem: Corresponding media pool item
        """
        ...

    def GetName(self) -> str:
        """Returns the timeline name.

        Returns:
            str: Timeline name
        """
        ...

    def GetNodeGraph(self) -> Graph:
        """Returns the timeline's node graph object.

        Returns:
            Graph: Node graph object
        """
        ...

    def GetSetting(self, settingName: Optional[str] = None) -> Union[str, dict]:
        """Returns value of timeline setting.

        Args:
            settingName (Optional[str], optional): Setting name to query. Defaults to None.

        Returns:
            Union[str, dict]: Setting value if name provided, else dictionary of all settings
        """
        ...

    def GetStartFrame(self) -> int:
        """Returns the frame number at the start of timeline.

        Returns:
            int: Start frame number
        """
        ...

    def GetStartTimecode(self) -> str:
        """Returns the start timecode for the timeline.

        Returns:
            str: Start timecode string
        """
        ...

    def GetTrackCount(self, trackType: str) -> int:
        """Gets number of tracks of specified type.

        Args:
            trackType (str): Type of track ("video" or "audio")

        Returns:
            int: Number of tracks
        """
        ...

    def GetTrackName(self, trackType: str, trackIndex: int) -> str:
        """Returns the track name.

        Args:
            trackType (str): Type of track ("audio", "video" or "subtitle")
            trackIndex (int): Index of track (1 <= trackIndex <= GetTrackCount(trackType))

        Returns:
            str: Track name
        """
        ...

    def GetTrackSubType(self, trackType: str, trackIndex: int) -> str:
        """Returns an audio track's format.

        Args:
            trackType (str): Type of track
            trackIndex (int): Index of track

        Returns:
            str: Audio track format string
        """
        ...

    def GetUniqueId(self) -> str:
        """Returns a unique ID for the timeline.

        Returns:
            str: Unique ID string
        """
        ...

    def GrabAllStills(self, stillFrameSource: int) -> list:
        """Grabs stills from all clips of the timeline.

        Args:
            stillFrameSource (int): Frame to grab (1 - First frame, 2 - Middle frame)

        Returns:
            list: List of GalleryStill objects
        """
        ...

    def GrabStill(self) -> GalleryStill:
        """Grabs still from the current video clip.

        Returns:
            GalleryStill: Gallery still object
        """
        ...

    # def ImportIntoTimeline(self, filePath: str, importOptions: Optional[dict] = None) -> bool:
    #     """Imports timeline items from file.

    #     Args:
    #         filePath (str): Path to import file
    #         importOptions (Optional[dict], optional): Dictionary of import options. Defaults to None.

            



    #     Returns:
    #         bool: True if successful
    #     """
    #     ...

    def ImportIntoTimeline(self, filePath: str, importOptions: dict = None) -> bool:
        """
        Imports timeline items from an AAF file with optional import options.

        Args:
            filePath (str): Path to import file
            importOptions (Optional[dict], optional): Dictionary of import options. Defaults to None.

        | Option                                        | Type    | Default       | Description                                                                                                           |
        | --------------------------------------------- | ------- | ------------- | --------------------------------------------------------------------------------------------------------------------- |
        | autoImportSourceClipsIntoMediaPool            | bool    | True          | Specifies if source clips should be imported into media pool                                                          |
        | ignoreFileExtensionsWhenMatching              | bool    | False         | Specifies if file extensions should be ignored when matching                                                          |
        | linkToSourceCameraFiles                       | bool    | False         | Specifies if link to source camera files should be enabled                                                            |
        | useSizingInfo                                 | bool    | False         | Specifies if sizing information should be used                                                                        |
        | importMultiChannelAudioTracksAsLinkedGroups   | bool    | False         | Specifies if multi-channel audio tracks should be imported as linked groups                                           |
        | insertAdditionalTracks                        | bool    | True          | Specifies if additional tracks should be inserted                                                                     |
        | insertWithOffset                              | str     | "00:00:00:00" | Specifies insert with offset value in timecode format, applicable if insertAdditionalTracks is False           |
        | sourceClipsPath                               | str     | None          | Filesystem path to search for source clips if media is inaccessible in original path                                  |
        | sourceClipsFolders                            | list    | None          | List of Media Pool folder objects to search for source clips if media is not in current folder                        |

         Returns:
             bool: True if successful

        """

    def InsertFusionCompositionIntoTimeline(self) -> TimelineItem:
        """Inserts a Fusion composition into the timeline.

        Returns:
            TimelineItem: The inserted timeline item
        """
        ...

    def InsertFusionGeneratorIntoTimeline(self, generatorName: str) -> TimelineItem:
        """Inserts a Fusion generator into the timeline.

        Args:
            generatorName (str): Name of generator to insert

        Returns:
            TimelineItem: The inserted timeline item
        """
        ...

    def InsertFusionTitleIntoTimeline(self, titleName: str) -> TimelineItem:
        """Inserts a Fusion title into the timeline.

        Args:
            titleName (str): Name of title to insert

        Returns:
            TimelineItem: The inserted timeline item
        """
        ...

    def InsertGeneratorIntoTimeline(self, generatorName: str) -> TimelineItem:
        """Inserts a generator into the timeline.

        Args:
            generatorName (str): Name of generator to insert

        Returns:
            TimelineItem: The inserted timeline item
        """
        ...

    def InsertOFXGeneratorIntoTimeline(self, generatorName: str) -> TimelineItem:
        """Inserts an OFX generator into the timeline.

        Args:
            generatorName (str): Name of generator to insert

        Returns:
            TimelineItem: The inserted timeline item
        """
        ...

    def InsertTitleIntoTimeline(self, titleName: str) -> TimelineItem:
        """Inserts a title into the timeline.

        Args:
            titleName (str): Name of title to insert

        Returns:
            TimelineItem: The inserted timeline item
        """
        ...

    def Print(self) -> Any:
        """Undocumented method.
        """
        ...

    def SetClipsLinked(self, timelineItems: list, linked: bool) -> bool:
        """Links or unlinks specified timeline items.

        Args:
            timelineItems (list): List of timeline items
            linked (bool): Whether to link or unlink

        Returns:
            bool: True if successful
        """
        ...

    def SetCurrentTimecode(self, timecode: str) -> bool:
        """Sets current playhead position from input timecode.

        Args:
            timecode (str): Timecode string

        Returns:
            bool: True if successful
        """
        ...

    def SetMarkInOut(self, inPoint: int, outPoint: int, type: str = "all") -> bool:
        """Sets mark in/out points.

        Args:
            inPoint (int): In point frame number
            outPoint (int): Out point frame number
            type (str, optional): Type of marks - "video", "audio" or "all". Defaults to "all".

        Returns:
            bool: True if successful
        """
        ...

    def SetName(self, timelineName: str) -> bool:
        """Sets the timeline name if timelineName is unique.

        Args:
            timelineName (str): New name for the timeline

        Returns:
            bool: True if successful
        """
        ...

    def SetSetting(self, settingName: str, settingValue: str) -> bool:
        """Sets timeline setting to the given value.

        Args:
            settingName (str): Name of setting to set
            settingValue (str): Value to set

        Returns:
            bool: True if successful
        """
        ...

    def SetStartTimecode(self, timecode: str) -> bool:
        """Set the start timecode of the timeline.

        Args:
            timecode (str): Timecode string

        Returns:
            bool: True if successful when the change is successful
        """
        ...

    def SetTrackEnable(self, trackType: str, trackIndex: int, enabled: bool) -> bool:
        """Enables/Disables track with given trackType and trackIndex.

        Args:
            trackType (str): Type of track ("audio", "video", "subtitle")
            trackIndex (int): Index of track (1 <= trackIndex <= GetTrackCount(trackType))
            enabled (bool): Whether to enable or disable the track

        Returns:
            bool: True if successful
        """
        ...

    def SetTrackLock(self, trackType: str, trackIndex: int, locked: bool) -> bool:
        """Locks/Unlocks track with given trackType and trackIndex.

        Args:
            trackType (str): Type of track ("audio", "video", "subtitle")
            trackIndex (int): Index of track (1 <= trackIndex <= GetTrackCount(trackType))
            locked (bool): Whether to lock or unlock the track

        Returns:
            bool: True if successful
        """
        ...

    def SetTrackName(self, trackType: str, trackIndex: int, name: str) -> bool:
        """Sets the track name.

        Args:
            trackType (str): Type of track ("audio", "video" or "subtitle")
            trackIndex (int): Index of track (1 <= trackIndex <= GetTrackCount(trackType))
            name (str): New name for the track

        Returns:
            bool: True if successful
        """
        ...

    def UpdateMarkerCustomData(self, frameId: int, customData: str) -> bool:
        """Updates customData for the marker at given frameId position.
        
        CustomData is not exposed via UI and is useful for scripting developer 
        to attach any user specific data to markers.

        Args:
            frameId (int): Frame ID of marker to update
            customData (str): New custom data string

        Returns:
            bool: True if successful
        """
        ...

class TimelineItem(PyRemoteObject):
    """A class representing an item in the timeline."""

    def AddFlag(self, color: str) -> bool:
        """Adds a flag with given color.
        
        Args:
            color (str): Color name for the flag

        Returns:
            bool: True if successful
        """
        ...

    def AddFusionComp(self) -> Any:
        """Adds a new Fusion composition associated with the timeline item.

        Returns:
            fusionComp: The created Fusion composition object
        """
        ...

    def AddMarker(self, frameId: int, color: str, name: str, note: str, 
                  duration: float, customData: Optional[str] = None) -> bool:
        """Creates a new marker at given frameId position with given marker information.
        
        Args:
            frameId (int): Frame position for the marker
            color (str): Color name for the marker
            name (str): Name of the marker
            note (str): Note text for the marker
            duration (float): Duration of the marker
            customData (str, optional): Custom data to attach to the marker

        Returns:
            bool: True if successful
        """
        ...

    def AddTake(self, media_pool_item: "MediaPoolItem", start_frame: Optional[int], 
                end_frame: Optional[int]) -> bool:
        """Adds mediaPoolItem as a new take. Initializes a take selector for the timeline 
        item if needed. By default, the full clip extents is added.

        Args:
            media_pool_item (MediaPoolItem): Media pool item to add as take
            start_frame (int, optional): Start frame position
            end_frame (int, optional): End frame position

        Returns:
            bool: True if successful
        """
        ...

    def AddVersion(self, versionName: str, versionType: int) -> bool:
        """Adds a new color version for a video clip.

        Args:
            versionName (str): Name for the new version
            versionType (int): Version type (0 - local, 1 - remote)

        Returns:
            bool: True if successful
        """
        ...

    def AssignToColorGroup(self, colorGroup: "ColorGroup") -> bool:
        """Returns True if item is successfully assigned to given ColorGroup.
        ColorGroup must be an existing group in the current project.
        
        Args:
            colorGroup (ColorGroup): The color group to assign this item to

        Returns:
            bool: True if successful
        """
        ...

    def ClearClipColor(self) -> bool:
        """Clears the item color.

        Returns:
            bool: True if successful
        """
        ...

    def ClearFlags(self, color: str) -> bool:
        """Clear flags of the specified color.
        
        Args:
            color (str): Color of flags to clear. Use "All" to clear all flags.

        Returns:
            bool: True if successful
        """
        ...

    def CopyGrades(self, targetTimelineItems: List["TimelineItem"]) -> bool:
        """Copies the current node stack layer grade to the same layer for each item 
        in targetTimelineItems.

        Args:
            targetTimelineItems (List[TimelineItem]): List of timeline items to copy grades to

        Returns:
            bool: True if successful
        """
        ...

    def CreateMagicMask(self, mode: str) -> bool:
        """Returns True if magic mask was created successfully.
        
        Args:
            mode (str): One of "F" (forward), "B" (backward), or "BI" (bidirection)

        Returns:
            bool: True if successful
        """
        ...

    def DeleteFusionCompByName(self, compName: str) -> bool:
        """Deletes the named Fusion composition.

        Args:
            compName (str): Name of the Fusion composition to delete

        Returns:
            bool: True if successful
        """
        ...

    def DeleteMarkerAtFrame(self, frameNum: int) -> bool:
        """Delete marker at frame number from the timeline item.
        
        Args:
            frameNum (int): Frame number to delete marker from

        Returns:
            bool: True if successful
        """
        ...

    def DeleteMarkerByCustomData(self, customData: str) -> bool:
        """Delete first matching marker with specified customData.
        
        Args:
            customData (str): Custom data string to match for deletion

        Returns:
            bool: True if successful
        """
        ...

    def DeleteMarkersByColor(self, color: str) -> bool:
        """Delete all markers of the specified color from the timeline item.
        
        Args:
            color (str): Color name of markers to delete. Use "All" to delete all color markers.

        Returns:
            bool: True if successful
        """
        ...

    def DeleteTakeByIndex(self, idx: int) -> bool:
        """Deletes a take by index.
        
        Args:
            idx (int): Index of take to delete. Must be between 1 and number of takes.

        Returns:
            bool: True if successful
        """
        ...

    def DeleteVersionByName(self, versionName: str, versionType: int) -> bool:
        """Deletes a color version by name and version type.
        
        Args:
            versionName (str): Name of version to delete
            versionType (int): Version type (0 - local, 1 - remote)

        Returns:
            bool: True if successful
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

    def FinalizeTake(self) -> bool:
        """
        Finalize take and discard the rest
        
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

    def GetDuration(self, subframe_precision: bool = False) -> Union[int, float]:
        """Returns the item duration.
        
        Args:
            subframe_precision (bool): If True, returns fractional frames

        Returns:
            Union[int, float]: Duration in frames (int) or fractional frames (float)
        """
        ...

    def GetEnd(self, subframe_precision: bool = False) -> Union[int, float]:
        """Returns the end frame position on the timeline.
        
        Args:
            subframe_precision (bool): If True, returns fractional frames

        Returns:
            Union[int, float]: End frame position (int) or fractional frame position (float)
        """
        ...

    def GetFlagList(self) -> List[str]:
        """Returns a list of flag colors assigned to the item.

        Returns:
            List[str]: List of flag color names
        """
        ...

    def GetFusionCompByIndex(self, compIndex: int) -> Any:
        """Returns the Fusion composition object based on given index.
        
        Args:
            compIndex (int): Index of composition to get (1 <= compIndex <= GetFusionCompCount())

        Returns:
            fusionComp: The Fusion composition object
        """
        ...

    def GetFusionCompByName(self, compName: str) -> Any:
        """Returns the Fusion composition object based on given name.

        Args:
            compName (str): Name of composition to get

        Returns:
            fusionComp: The Fusion composition object
        """
        ...

    def GetFusionCompCount(self) -> int:
        """Returns number of Fusion compositions associated with the timeline item.

        Returns:
            int: Number of Fusion compositions
        """
        ...

    def GetFusionCompNameList(self) -> List[str]:
        """Returns a list of Fusion composition names associated with the timeline item.

        Returns:
            List[str]: List of composition names
        """
        ...

    def GetIsColorOutputCacheEnabled(self) -> Any:
        """Returns if the color output cache is enabled.

        Returns:
            Any: Cache value indicating if enabled
        """
        ...

    def GetIsFusionOutputCacheEnabled(self) -> Any:
        """Returns if the Fusion output cache is enabled (or auto).

        Returns:
            Any: Cache value indicating if enabled/auto
        """
        ...

    def GetLeftOffset(self, subframe_precision: bool = False) -> Union[int, float]:
        """Returns the maximum extension by frame for clip from left side.
        
        Args:
            subframe_precision (bool): If True, returns fractional frames

        Returns:
            Union[int, float]: Maximum left extension in frames (int) or fractional frames (float)
        """
        ...

    def GetLinkedItems(self) -> List["TimelineItem"]:
        """Returns a list of linked timeline items.

        Returns:
            List[TimelineItem]: List of linked timeline items
        """
        ...

    def GetMarkerByCustomData(self, customData: str) -> Dict[str, Any]:
        """Returns marker information for the first matching marker with specified customData.
        
        Args:
            customData (str): Custom data string to match

        Returns:
            Dict[str, Any]: Dictionary containing marker information
        """
        ...

    def GetMarkerCustomData(self, frameId: int) -> str:
        """Returns customData string for the marker at given frameId position.
        
        Args:
            frameId (int): Frame ID of the marker

        Returns:
            str: Custom data string for the marker
        """
        ...

    def GetMarkers(self) -> Dict[float, Dict[str, Any]]:
        """Returns a dict (frameId -> {information}) of all markers and dicts with their information.
        Example: {96.0: {'color': 'Green', 'duration': 1.0, 'note': '', 'name': 'Marker 1', 'customData': ''}}
        indicates a single green marker at clip offset 96

        Returns:
            Dict[float, Dict[str, Any]]: Dictionary mapping frame IDs to marker information
        """
        ...

    def GetMediaPoolItem(self) -> "MediaPoolItem":
        """Returns the media pool item corresponding to the timeline item if one exists.

        Returns:
            MediaPoolItem: Corresponding media pool item
        """
        ...

    def GetName(self) -> str:
        """Returns the clip name.

        Returns:
            str: Clip name
        """
        ...

    def GetNodeGraph(self, layerIdx: Optional[int] = None) -> Any:
        """Returns the clip's node graph object at layerIdx.
        
        Args:
            layerIdx (int, optional): Layer index (1 <= layerIdx <= project.GetSetting("nodeStackLayers"))
                                    Returns the first layer if layerIdx is skipped.

        Returns:
            Graph: The node graph object
        """
        ...

    def GetProperty(self, propertyKey: Optional[str] = None) -> Union[int, Dict[str, Any]]:
        """Returns the value of property or all properties.

        | Property         | Type  | Range                      |
        | ---------------- | ----- | ---------------------------|
        | Pan              | float | (-4.0*width to 4.0*width)  |
        | Tilt             | float | (-4.0*height to 4.0*height)|
        | ZoomX            | float | (0.0 to 100.0)             |
        | ZoomY            | float | (0.0 to 100.0)             |
        | ZoomGang         | bool  |                            |
        | RotationAngle    | float | (-360.0 to 360.0)          |
        | AnchorPointX     | float | (-4.0*width to 4.0*width)  |
        | AnchorPointY     | float | (-4.0*height to 4.0*height)|
        | Pitch            | float | (-1.5 to 1.5)              |
        | Yaw              | float | (-1.5 to 1.5)              |
        | FlipX            | bool  |                            |
        | FlipY            | bool  |                            |
        | CropLeft         | float | (0.0 to width)             |
        | CropRight        | float | (0.0 to width)             |
        | CropTop          | float | (0.0 to height)            |
        | CropBottom       | float | (0.0 to height)            |
        | CropSoftness     | float | (-100.0 to 100.0)          |
        | CropRetain       | bool  |                            |
        | DynamicZoomEase  | int   | (0-3)                      |
        | CompositeMode    | int   | (0-31)                     |
        | Opacity          | float | (0.0 to 100.0)             |
        | Distortion       | float | (-1.0 to 1.0)              |
        | RetimeProcess    | int   | (0-3)                      |
        | MotionEstimation | int   | (0-6)                      |
        | Scaling          | int   | (0-4)                      |
        | ResizeFilter     | int   | (0-15)                     |

        Args:
            propertyKey (str, optional): Property key to get value for. If None, returns all properties.

        Returns:
            Union[int, Dict[str, Any]]: Property value or dictionary of all properties
        """
        ...

    def GetRightOffset(self, subframe_precision: bool = False) -> Union[int, float]:
        """Returns the maximum extension by frame for clip from right side.
        
        Args:
            subframe_precision (bool): If True, returns fractional frames

        Returns:
            Union[int, float]: Maximum right extension in frames (int) or fractional frames (float)
        """
        ...

    def GetSelectedTakeIndex(self) -> int:
        """Returns the index of the currently selected take, or 0 if the clip is not a take selector.

        Returns:
            int: Selected take index
        """
        ...

    def GetSourceAudioChannelMapping(self) -> str:
        """Returns a string with TimelineItem's audio mapping information.

        Returns:
            str: JSON formatted string containing audio mapping information
        """
        ...

    def GetSourceEndFrame(self) -> int:
        """Returns the end frame position of the media pool clip in the timeline clip.

        Returns:
            int: End frame position
        """
        ...

    def GetSourceEndTime(self) -> float:
        """Returns the end time position of the media pool clip in the timeline clip.

        Returns:
            float: End time position
        """
        ...

    def GetSourceStartFrame(self) -> int:
        """Returns the start frame position of the media pool clip in the timeline clip.

        Returns:
            int: Start frame position
        """
        ...

    def GetSourceStartTime(self) -> float:
        """Returns the start time position of the media pool clip in the timeline clip.

        Returns:
            float: Start time position
        """
        ...

    def GetStart(self, subframe_precision: bool = False) -> Union[int, float]:
        """Returns the start frame position on the timeline.
        
        Args:
            subframe_precision (bool): If True, returns fractional frames

        Returns:
            Union[int, float]: Start frame position (int) or fractional frame position (float)
        """
        ...

    def GetStereoConvergenceValues(self) -> Dict[Any, Any]:
        """Returns a dict (offset -> value) of keyframe offsets and respective convergence values.

        Returns:
            Dict[Any, Any]: Dictionary mapping offsets to convergence values
        """
        ...

    def GetStereoLeftFloatingWindowParams(self) -> Dict[Any, Dict[str, Any]]:
        """For the LEFT eye -> returns a dict (offset -> dict) of keyframe offsets and respective 
        floating window params. Value at particular offset includes the left, right, top and bottom 
        floating window values.

        Returns:
            Dict[Any, Dict[str, Any]]: Dictionary mapping offsets to floating window parameters
        """
        ...

    def GetStereoRightFloatingWindowParams(self) -> Dict[Any, Dict[str, Any]]:
        """For the RIGHT eye -> returns a dict (offset -> dict) of keyframe offsets and respective 
        floating window params. Value at particular offset includes the left, right, top and bottom 
        floating window values.

        Returns:
            Dict[Any, Dict[str, Any]]: Dictionary mapping offsets to floating window parameters
        """
        ...

    def GetTakeByIndex(self, idx: int) -> Dict[str, Any]:
        """Returns a dict with take info for specified index.
        
        Args:
            idx (int): Take index (1 <= idx <= number of takes)

        Returns:
            Dict[str, Any]: Dictionary with keys "startFrame", "endFrame" and "mediaPoolItem"
        """
        ...

    def GetTakesCount(self) -> int:
        """Return the number of takes in take selector, or 0 if the clip is not a take selector.

        Returns:
            int: Number of takes
        """
        ...

    def GetTrackTypeAndIndex(self) -> List[Union[str, int]]:
        """Returns a list of two values that correspond to the TimelineItem's trackType and trackIndex.
        
        Returns:
            List[Union[str, int]]: [trackType (str), trackIndex (int)] where
                trackType is one of {"audio", "video", "subtitle"}
                1 <= trackIndex <= Timeline.GetTrackCount(trackType)
        """
        ...

    def GetVersionNameList(self, versionType: int) -> List[str]:
        """Returns a list of all color versions for the given versionType.
        
        Args:
            versionType (int): Version type (0 - local, 1 - remote)

        Returns:
            List[str]: List of version names
        """
        ...

    def ImportFusionComp(self, path: str) -> Any:
        """Imports a Fusion composition from given file path by creating and adding 
        a new composition for the item.
        
        Args:
            path (str): File path to import composition from

        Returns:
            fusionComp: The imported Fusion composition object
        """
        ...

    def LoadBurnInPreset(self, presetName: str) -> bool:
        """Loads user defined data burn in preset for clip.
        
        Args:
            presetName (str): Name of preset to load

        Returns:
            bool: True if successful
        """
        ...

    def LoadFusionCompByName(self, compName: str) -> Any:
        """Loads the named Fusion composition as the active composition.
        
        Args:
            compName (str): Name of composition to load

        Returns:
            fusionComp: The loaded Fusion composition object
        """
        ...

    def LoadVersionByName(self, versionName: str, versionType: int) -> bool:
        """Loads a named color version as the active version.
        
        Args:
            versionName (str): Name of version to load
            versionType (int): Version type (0 - local, 1 - remote)

        Returns:
            bool: True if successful
        """
        ...

    def RegenerateMagicMask(self) -> bool:
        """Returns True if magic mask was regenerated successfully.

        Returns:
            bool: True if successful
        """
        ...

    def RemoveFromColorGroup(self) -> bool:
        """Returns True if the item is successfully removed from its ColorGroup.

        Returns:
            bool: True if successful
        """
        ...

    def RenameFusionCompByName(self, oldName: str, newName: str) -> bool:
        """Renames the Fusion composition identified by oldName.
        
        Args:
            oldName (str): Current name of composition
            newName (str): New name for composition

        Returns:
            bool: True if successful
        """
        ...

    def RenameVersionByName(self, oldName: str, newName: str, versionType: int) -> bool:
        """Renames the color version identified by oldName and versionType.
        
        Args:
            oldName (str): Current name of version
            newName (str): New name for version
            versionType (int): Version type (0 - local, 1 - remote)

        Returns:
            bool: True if successful
        """
        ...

    def SelectTakeByIndex(self, idx: int) -> bool:
        """Selects a take by index.
        
        Args:
            idx (int): Take index (1 <= idx <= number of takes)

        Returns:
            bool: True if successful
        """
        ...

    def SetCDL(self, cdlMap: Dict[str, str]) -> bool:
        """Sets CDL values according to provided map.
        
        Args:
            cdlMap (Dict[str, str]): Dictionary with keys:
                "NodeIndex": str (1 <= NodeIndex <= total number of nodes)
                "Slope": str (e.g. "0.5 0.4 0.2")
                "Offset": str (e.g. "0.4 0.3 0.2")
                "Power": str (e.g. "0.6 0.7 0.8")
                "Saturation": str (e.g. "0.65")

        Returns:
            bool: True if successful
        """
        ...

    def SetClipColor(self, colorName: str) -> bool:
        """Sets the item color based on the colorName.
        
        Args:
            colorName (str): Name of color to set

        Returns:
            bool: True if successful
        """
        ...

    def SetClipEnabled(self, enabled: bool) -> bool:
        """Sets clip enabled based on argument.
        
        Args:
            enabled (bool): Whether to enable the clip

        Returns:
            bool: True if successful
        """
        ...

    def SetColorOutputCache(self, cache_value: Any) -> bool:
        """Sets color output caching to enabled or disabled.
        
        Args:
            cache_value: Cache value to set

        Returns:
            bool: True if successful
        """
        ...

    def SetFusionOutputCache(self, cache_value: Any) -> bool:
        """Sets Fusion output caching to auto, enabled or disabled.
        
        Args:
            cache_value: Cache value to set

        Returns:
            bool: True if successful
        """
        ...

    def SetProperty(self, propertyKey: str, propertyValue: Any) -> bool:
        """Sets the value of property.

                | Property         | Type  | Range                      |
        | ---------------- | ----- | ---------------------------|
        | Pan              | float | (-4.0*width to 4.0*width)  |
        | Tilt             | float | (-4.0*height to 4.0*height)|
        | ZoomX            | float | (0.0 to 100.0)             |
        | ZoomY            | float | (0.0 to 100.0)             |
        | ZoomGang         | bool  |                            |
        | RotationAngle    | float | (-360.0 to 360.0)          |
        | AnchorPointX     | float | (-4.0*width to 4.0*width)  |
        | AnchorPointY     | float | (-4.0*height to 4.0*height)|
        | Pitch            | float | (-1.5 to 1.5)              |
        | Yaw              | float | (-1.5 to 1.5)              |
        | FlipX            | bool  |                            |
        | FlipY            | bool  |                            |
        | CropLeft         | float | (0.0 to width)             |
        | CropRight        | float | (0.0 to width)             |
        | CropTop          | float | (0.0 to height)            |
        | CropBottom       | float | (0.0 to height)            |
        | CropSoftness     | float | (-100.0 to 100.0)          |
        | CropRetain       | bool  |                            |
        | DynamicZoomEase  | int   | (0-3)                      |
        | CompositeMode    | int   | (0-31)                     |
        | Opacity          | float | (0.0 to 100.0)             |
        | Distortion       | float | (-1.0 to 1.0)              |
        | RetimeProcess    | int   | (0-3)                      |
        | MotionEstimation | int   | (0-6)                      |
        | Scaling          | int   | (0-4)                      |
        | ResizeFilter     | int   | (0-15)                     |

        Args:
            propertyKey (str): Property key to set
            propertyValue (Any): Value to set for the property

        Returns:
            bool: True if successful
        """
        ...

    def SmartReframe(self) -> bool:
        """Performs Smart Reframe.

        Returns:
            bool: True if successful
        """
        ...

    def Stabilize(self) -> bool:
        """Performs stabilization.

        Returns:
            bool: True if successful
        """
        ...

    def UpdateMarkerCustomData(self, frameId: int, customData: str) -> bool:
        """Updates customData for the marker at given frameId position.
        
        Args:
            frameId (int): Frame ID of marker to update
            customData (str): New custom data string

        Returns:
            bool: True if successful
        """
        ...

    def UpdateSidecar(self) -> bool:
        """Updates sidecar file for BRAW clips or RMD file for R3D clips.

        Returns:
            bool: True if successful
        """
        ...


class Graph(PyRemoteObject):
    """Class representing a node graph for color operations in DaVinci Resolve."""

    def ApplyArriCdlLut(self) -> bool:
        """Applies ARRI CDL and LUT.

        Returns:
            bool: True if successful, False otherwise
        """
        ...

    def ApplyGradeFromDRX(self, path: str, gradeMode: int) -> bool:
        """Loads a still from given file path and applies grade to graph with specified mode.

        Args:
            path (str): File path to DRX file
            gradeMode (int): Grade application mode:
                            0 - No keyframes
                            1 - Source Timecode aligned
                            2 - Start Frames aligned

        Returns:
            bool: True if successful
        """
        ...

    def GetLUT(self, nodeIndex: int) -> str:
        """Gets relative LUT path based on the node index provided.

        Args:
            nodeIndex (int): Node index (1 <= nodeIndex <= total number of nodes)

        Returns:
            str: Relative LUT path
        """
        ...

    def GetNodeLabel(self, nodeIndex: int) -> str:
        """Returns the label of the node at nodeIndex.

        Args:
            nodeIndex (int): Node index

        Returns:
            str: Node label
        """
        ...

    def GetNumNodes(self) -> int:
        """Returns the number of nodes in the graph.

        Returns:
            int: Number of nodes
        """
        ...

    def ResetAllGrades(self) -> bool:
        """Resets all grades in the graph.

        Returns:
            bool: True if all grades were reset successfully, False otherwise
        """
        ...

    def SetLUT(self, nodeIndex: int, lutPath: str) -> bool:
        """Sets LUT on the node mapping the node index provided.

        The lutPath can be an absolute path, or a relative path (based off custom LUT paths 
        or the master LUT path). The operation is successful for valid lut paths that 
        Resolve has already discovered (see Project.RefreshLUTList).

        Args:
            nodeIndex (int): Node index (1 <= nodeIndex <= self.GetNumNodes())
            lutPath (str): Path to LUT file

        Returns:
            bool: True if successful
        """
        ...

    def SetNodeEnabled(self, nodeIndex: int, isEnabled: bool) -> bool:
        """Sets the node at the given nodeIndex to enabled or disabled.

        Args:
            nodeIndex (int): Node index (1 <= nodeIndex <= self.GetNumNodes())
            isEnabled (bool): Whether to enable or disable the node

        Returns:
            bool: True if successful
        """
        ...

class ColorGroup(PyRemoteObject):
    """Class representing a color group in DaVinci Resolve."""
    
    def GetName(self) -> str:
        """Returns the name of the ColorGroup.
        
        Returns:
            str: Name of the color group
        """
        ...
        
    def SetName(self, groupName: str) -> bool:
        """Renames ColorGroup.
        
        Args:
            groupName (str): New name for the color group
            
        Returns:
            bool: True if successful
        """
        ...
        
    def GetClipsInTimeline(self, timeline: Optional["Timeline"] = None) -> List["TimelineItem"]:
        """Returns a list of TimelineItem that are in colorGroup in the given Timeline.
        
        Args:
            timeline (Timeline, optional): Timeline to get clips from. Defaults to Current Timeline.
            
        Returns:
            List[TimelineItem]: List of timeline items in this color group
        """
        ...
        
    def GetPreClipNodeGraph(self) -> "Graph":
        """Returns the ColorGroup Pre-clip graph.
        
        Returns:
            Graph: The pre-clip node graph
        """
        ...
        
    def GetPostClipNodeGraph(self) -> "Graph":
        """Returns the ColorGroup Post-clip graph.
        
        Returns:
            Graph: The post-clip node graph
        """
        ...

class GalleryStill(PyRemoteObject):
    """Undocumented class.
    """
    pass