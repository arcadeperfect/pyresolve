from .pyresolve import Kernel, ShotBin, SequenceBin, SortMode
from .get_resolve import GetResolve

# """
# Instructions to use this library from within Resolve:

# Place references in the Resolve scripts folder:
# C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility

# These scripts need no logic, they can just reference functions in this file, which will hook into the library.
# This makes developtment a lot eaiser and prevents the need to repeat code. 

# For example, create a script in the Resolve dierctory with the folloing:

# ### version_up.py ### 

# >>> import sys
# >>> sys.path.append("C:\\PATH\\TO\\PARENT\\DIRECTORY\\OF\\THIS\\LIBRARY") 
# >>> from pyresolve_hornet import entry_point
# >>> entry_point.version_up()

# ### version_down.py ### 

# >>> import sys
# >>> sys.path.append("C:\\PATH\\TO\\PARENT\\DIRECTORY\\OF\\THIS\\LIBRARY") 
# >>> from pyresolve_hornet import entry_point
# >>> entry_point.version_down()


# The path you append to sys.path is the parent folder of the pyresolve_hornet folder. For example:

# >>> sys.path.append("C:\\Users\\alexh\\src\\pyresolve_hornet\\src")

# """


def version_up():
    
    resolve = GetResolve()
    kernel = Kernel(resolve)

    current_item = kernel.active_timeline_item

    shot_bin = ShotBin.from_timeline_item(current_item, kernel)
    shot_bin.version_up(current_item, SortMode.VERSIONPARSE)

    pass


def version_down():
    resolve = GetResolve()
    kernel = Kernel(resolve)

    current_item = kernel.active_timeline_item

    shot_bin = ShotBin.from_timeline_item(current_item, kernel)
    shot_bin.version_down(current_item, SortMode.VERSIONPARSE)

    pass