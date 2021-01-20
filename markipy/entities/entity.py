from dataclasses import dataclass
from .base import Logger, Configuration
from .base import Time, Path


@dataclass(init=False, unsafe_hash=True)
class Entity(Logger, Configuration):
    time: Time = Time
    path: Path = Path

    def __init__(self, **kwards):
        Configuration.__init__(self, **kwards)
        Logger.__init__(self, **kwards)

