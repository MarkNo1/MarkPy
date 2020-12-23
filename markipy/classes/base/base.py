from dataclasses import dataclass

from ..time import Time
from .base_meta import BaseMeta


@dataclass
class BaseClass(BaseMeta):

    def __del__(self):
        self._class_deletion_date = Time.now()
