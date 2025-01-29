import sys
from pathlib import Path
sys.path.append(str(Path(r"P:\dev\alexh_dev\resolve\pyresolve\src")))

from pyresolve import entry_point


entry_point.latest_versions_on_tracks()