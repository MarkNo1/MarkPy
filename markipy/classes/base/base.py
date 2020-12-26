from dataclasses import dataclass

from ..time import Time
from .base_meta import BaseMeta


@dataclass(init=False, unsafe_hash=True)
class BaseClass(BaseMeta):

    def __del__(self):
        self._class_deletion_date = Time.now()

    def __init__(self, **kwargs):
        BaseMeta.__init__(self, **kwargs)