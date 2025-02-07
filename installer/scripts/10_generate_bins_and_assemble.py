import sys
from pathlib import Path
sys.path.append(str(Path(r"P:\dev\alexh_dev\resolve\pyresolve\src")))

from pyresolve import entry_point

entry_point.generate_bins_and_assemble()