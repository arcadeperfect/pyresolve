from typing import Optional, List, Dict, Any, Protocol, TypedDict, Union, overload



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

    def GetClipList(self) -> List[MediaPoolItem]:
        
        """Returns a list of MediaPoolItem objects that are children of this folder."""
        ...

    def GetClips(self) -> dict[int, MediaPoolItem]:
        """
        Return a dictionary of the contained MediaPoolItems with integers as the keys,
        starting from 1
        
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

    def GetSubFolders(self) -> dict[int, Folder]:
        """
        Return a dictionary of the contained Folders with integers as the keys,
        starting from 1
        
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

    

class MediaPoolItem(PyRemoteObject):
    

    #def GetClipProperty(self, key: str) -> Dict[str, Any]:
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

   

    def GetName(self) -> str:
        """        
        File name. Not modifiable. Distinct from the display name returned
        by TimelineItem. Not necessarily unique.
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

    
    @overload
    def SetThirdPartyMetadata(self, key: str, value: str) -> bool:
        """
        Set arbitrary metadata by specifying key and value as separate arguments
        
        """
        ...
    @overload
    def SetThirdPartyMetadata(self, data: dict[str, str]) -> bool:
        """
        Set arbitrary metadata by passing a dictionary, to be concatinated with existing data
        
        """
        ...

    

class MediaStorage(PyRemoteObject):
    """TODO: Add docstring."""

class Project(PyRemoteObject):
    """TODO: Add docstring."""

    

class ProjectManager(PyRemoteObject):
    """TODO: Add docstring."""

    

class Resolve(PyRemoteObject):
    """Resolve app instance."""

    

    

class Timeline(PyRemoteObject):
    """TODO: Add docstring."""

    def AddTrack(self, trackType: str) -> bool:
        """
        Add a track

        Args:
            trackType (str): The type of track to add: "video", "audio", "subtitle"

        Returns:
            bool: True if successful
        """
        ...

    

    def GetItemListInTrack(self, trackType: str, index: int) -> Optional[list[TimelineItem]]:
        """
        Args:
            trackType (str): "video" or "audio"?
            index (int): index of the track, starting from 1
        Returns:
            list[TimelineItem]: list of TimeLineItems in specified track
        """
        ...

    def GetItemsInTrack(self, trackType: str, index: int) -> dict[int, TimelineItem]:
        """
        Args:
            trackType (str): "video" or "audio"?
            index (int): index of the track, starting from 1
        Returns:
            dict[int, TimelineItem]: dict of TimeLineItems in specified track with integers as keys, starting from 1
        """
        ...

    

    def GetTrackCount(self, trackType: str) -> int:
        """
        Args:
            trackType (str): "video" or "audio"?
        Returns:
            int: number of tracks
        
        """
        ...

    

    def SetTrackName(self, name: str, track_index: int, new_name: str) -> bool:
        """
        Args:
            name (str): "video" or "audio"?
            track_index (int): index of the track, starting from 1
            new_name (str): name of the new track

        Returns:
            bool: True if successful

        """
        ...

    

class TimelineItem(PyRemoteObject):
    """TODO: Add docstring."""

    

    def AddTake(self, 
                media_pool_item: "MediaPoolItem", 
                start_frame: Optional[int], 
                end_frame: Optional[int]) -> bool:
        """
        Adds a new take to take selector. It will initialise this timeline item as take selector if it’s not already one. Arguments startFrame and endFrame are optional, and if not specified the entire clip will be added.

        Args:
            media_pool_item (MediaPoolItem): Media pool item
            start_frame (int): Start frame
            end_frame (int): End frame

        Returns:
            bool    
        
        """
        ...

    

    def FinalizeTake(self) -> bool:
        """
        Finalize take and discard the rest
        
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

    

    def GetProperty(self) -> Dict[str, Any]:
        """
        Properties dictionary. Available keys:

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
            
        Returns:
            Dict[str, Any]
        """
        ...

    

    def GetSourceEndFrame(self) -> int:
        """
        Get the out point of the source clip in the current timeline item.
        
        """
        ...

   

    def GetSourceStartFrame(self) -> int:
        """
        Get the in point of the source clip in the current timeline item.
        
        """
        ...

    

    def GetTakesCount(self) -> int:
        """
        Return the number of takes in the current timeline item
        A take is an instance of MediaPoolItem
        """
        ...

    

    def SelectTakeByIndex(self, int) -> bool:
        """
        Select a take by index
        
        """
        ...

   