from enum import Enum, auto
from pathlib import Path
from lazy_prop import lazy_property
from file_sequence import FileSequence, Components

from resolve_stubs.types import Resolve


class Kernel:
    def __init__(self, resolve_instance: Resolve):

        self.resolve = resolve_instance