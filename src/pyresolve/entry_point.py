from .pyresolve import Kernel, ShotBin, SequenceBin, SortMode
from .get_resolve import GetResolve

import tkinter as tk
from tkinter import messagebox, simpledialog

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
# print(mpi.SetClipProperty("Clip Name", "hello"))
def message():
    resolve = GetResolve()
    kernel = Kernel(resolve)

    root = tk.Tk()
    root.withdraw()

    user_input = simpledialog.askstring("Message", "Enter message")

    mpi = kernel.active_timeline_item.GetMediaPoolItem()
    mpi.SetClipProperty("Clip Name", user_input)


def version_up():
    
    resolve = GetResolve()
    kernel = Kernel(resolve)

    current_item = kernel.active_timeline_item

    if current_item is None:
        return

    shot_bin = ShotBin.from_timeline_item(current_item, kernel)
    shot_bin.version_up(current_item, SortMode.VERSIONPARSE)




def version_down():
    resolve = GetResolve()
    kernel = Kernel(resolve)

    current_item = kernel.active_timeline_item

    if current_item is None:
        return
    
    shot_bin = ShotBin.from_timeline_item(current_item, kernel)
    shot_bin.version_down(current_item, SortMode.VERSIONPARSE)



def latest_version():
    resolve = GetResolve()
    kernel = Kernel(resolve)
    current_item = kernel.active_timeline_item

    if current_item is None:
        return
    shot_bin = ShotBin.from_timeline_item(current_item, kernel)
    shot_bin.version_latest(current_item, SortMode.VERSIONPARSE)

    pass


def oldest_version():
    resolve = GetResolve()
    kernel = Kernel(resolve)
    current_item = kernel.active_timeline_item

    if current_item is None:
        return
    shot_bin = ShotBin.from_timeline_item(current_item, kernel)
    shot_bin.version_oldest(current_item, SortMode.VERSIONPARSE)


    pass


