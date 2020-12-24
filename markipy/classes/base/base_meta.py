import dataclasses

from ..time import Time
from ..path import Path


def safe_init_meta_class(cls, kwargs):
    names = set([f.name for f in dataclasses.fields(cls)])
    for k, v in kwargs.items():
        if k in names:
            setattr(cls, k, v)


@dataclasses.dataclass(unsafe_hash=True, init=False)
class BaseMeta:
    _class_name: str = 'BaseMeta'
    _class_version: str = '0.0.1'
    _class_creation_date: str = Time.now()
    _class_deletion_date: str = "nan"
    _class_creation_path: Path = Path().cwd()
    _class_working_path: Path = Path.cwd()

    def __init__(self, **kwargs):
        safe_init_meta_class(self, kwargs)
