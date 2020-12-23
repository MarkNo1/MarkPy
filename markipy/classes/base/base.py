from .base_meta import BaseMeta
from ..time import Time


class BaseClass(object):
    def __init__(self, meta_class: BaseMeta):
        self._meta_class = meta_class

    def __del__(self):
        self._meta_class._class_deletion_date = Time.now()
