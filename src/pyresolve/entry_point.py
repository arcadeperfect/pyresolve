from .pyresolve import (
    Kernel,
    ShotBin,
    SequenceBin,
    SortMode,
    version_up_tracks as _version_up_tracks,
    version_down_tracks as _version_down_tracks,
    version_latest_tracks,
    version_oldest_tracks,
    FileType
)
from .get_resolve import GetResolve
from pathlib import Path
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




def generate_bins():
    resolve = GetResolve()
    kernel = Kernel(resolve)

    name, path, subpath, file_type = _get_path_and_subPath()

    path = Path(_clean_slashes(path))
    subpath = Path(_clean_slashes(subpath))


    if any(x is None for x in (name, path, subpath, file_type)):
        return


    if file_type.lower() == "mov":
        ft = FileType.MOV

    elif file_type.lower() == "dpx":
        ft = FileType.DPX

    elif file_type.lower() == "exr":
        ft = FileType.EXR


    # try:
    #     f = str(file_type).upper()
    #     ft = FileType[f]
    
    # except KeyError:
    #     print("Invalid file type")
    #     return

    print(ft)

    sb = SequenceBin(
        name=name,
        sequence_root_path=path,
        sub_path=subpath,
        file_type=ft,
        parent_bin=kernel.root_folder,
        kernel=kernel,
    )

    sb.create_folder()
    sb.create_shot_bins()
    sb.populate_shot_bins(1)

def generate_bins_and_assemble():
    resolve = GetResolve()
    kernel = Kernel(resolve)

    if kernel.current_timeline is None:
        #TODO add error popup
        return
    

    name, path, subpath, file_type = _get_path_and_subPath()

    path = Path(_clean_slashes(path))
    subpath = Path(_clean_slashes(subpath))


    if any(x is None for x in (name, path, subpath, file_type)):
        return


    if file_type.lower() == "mov":
        ft = FileType.MOV

    elif file_type.lower() == "dpx":
        ft = FileType.DPX

    elif file_type.lower() == "exr":
        ft = FileType.EXR



    print(ft)

    sb = SequenceBin(
        name=name,
        sequence_root_path=path,
        sub_path=subpath,
        file_type=ft,
        parent_bin=kernel.root_folder,
        kernel=kernel,
    )

    sb.create_folder()
    sb.create_shot_bins()
    sb.populate_shot_bins(4)
    sb.assemble_timeline(track=1, handle=0)

def latest_versions_on_tracks():
    resolve = GetResolve()
    kernel = Kernel(resolve)

    existing_tracks = kernel.get_existing_track_indices()

    selection = _get_checkbox_values(existing_tracks)

    version_latest_tracks(selection, kernel)


def oldest_versions_on_tracks():
    resolve = GetResolve()
    kernel = Kernel(resolve)

    existing_tracks = kernel.get_existing_track_indices()

    selection = _get_checkbox_values(existing_tracks)

    version_oldest_tracks(selection, kernel)


def version_up_tracks():
    resolve = GetResolve()
    kernel = Kernel(resolve)

    existing_tracks = kernel.get_existing_track_indices()

    selection = _get_checkbox_values(existing_tracks)

    _version_up_tracks(selection, kernel)


def version_down_tracks():
    resolve = GetResolve()
    kernel = Kernel(resolve)

    existing_tracks = kernel.get_existing_track_indices()

    selection = _get_checkbox_values(existing_tracks)

    _version_down_tracks(selection, kernel)

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


def _get_checkbox_values(numbers):


    #TODO invert order of checkboxes

    selections = []
    window = tk.Tk()
    window.attributes("-topmost", True)

    message = tk.Label(window, text="Select tracks to process:")
    message.pack()

    for num in numbers:
        var = tk.BooleanVar()
        selections.append(var)
        tk.Checkbutton(window, text=str(num), variable=var).pack()

    results = []

    def on_submit():
        results.extend([var.get() for var in selections])
        window.destroy()

    tk.Button(window, text="Submit", command=on_submit).pack()
    window.mainloop()

    output = []

    for i in range(len(selections)):
        if selections[i].get():
            output.append(numbers[i])

    return output

def _get_path_and_subPath():
    window = tk.Tk()
    window.attributes("-topmost", True)

    message = tk.Label(window, text="Enter path information:")
    message.pack()

    #TODO use file browsers instead of string field

    # Create frame for name entry
    name_frame = tk.Frame(window)
    name_frame.pack(pady=5)
    tk.Label(name_frame, text="Name:").pack(side=tk.LEFT)
    name_var = tk.StringVar()
    name_entry = tk.Entry(name_frame, textvariable=name_var)
    name_entry.pack(side=tk.LEFT, padx=5)

    # Create frame for path entry
    path_frame = tk.Frame(window)
    path_frame.pack(pady=5)
    tk.Label(path_frame, text="Path:").pack(side=tk.LEFT)
    path_var = tk.StringVar()
    path_entry = tk.Entry(path_frame, textvariable=path_var)
    path_entry.pack(side=tk.LEFT, padx=5)

    # Create frame for sub path entry
    subpath_frame = tk.Frame(window)
    subpath_frame.pack(pady=5)
    tk.Label(subpath_frame, text="Sub Path:").pack(side=tk.LEFT)
    subpath_var = tk.StringVar()
    subpath_entry = tk.Entry(subpath_frame, textvariable=subpath_var)
    subpath_entry.pack(side=tk.LEFT, padx=5)

    # Create frame for file type entry
    fileType_frame = tk.Frame(window)
    fileType_frame.pack(pady=5)
    tk.Label(fileType_frame, text="File extension:").pack(side=tk.LEFT)
    filetype_var = tk.StringVar()
    filetype_entry = tk.Entry(fileType_frame, textvariable=filetype_var)
    filetype_entry.pack(side=tk.LEFT, padx=5)

    results = []

    def on_submit():
        # Fixed: removed duplicate subpath_var.get()
        results.extend([name_var.get(), path_var.get(), subpath_var.get(), filetype_var.get()])
        window.destroy()

    tk.Button(window, text="Submit", command=on_submit).pack(pady=10)
    window.mainloop()

    # Fixed: return None * 4 instead of None * 2 to match the number of values
    return results if results else [None] * 4


def _clean_slashes(path_str):
    # return path_str.strip('\/').strip()
    return path_str.strip()