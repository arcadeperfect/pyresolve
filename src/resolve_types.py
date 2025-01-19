from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Protocol
    
    class Timeline(Protocol):
        pass
        
    class MediaPool(Protocol):
        pass