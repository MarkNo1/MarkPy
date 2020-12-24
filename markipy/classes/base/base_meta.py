import dataclasses
from random import randint

from ..time import Time
from ..path import Path


def safe_init_meta_class(cls, kwargs):
    names = set([f.name for f in dataclasses.fields(cls)])
    for k, v in kwargs.items():
        if k in names:
            setattr(cls, k, v)


def update_kwargs_param_if_needed(kwargs, new_kwargs):
    for k, v in new_kwargs.items():
        if k not in kwargs:
            kwargs.update({k: v})
    return kwargs


@dataclasses.dataclass(unsafe_hash=True, init=False)
class BaseMeta:
    _class_name: str = 'BaseMeta'
    _class_version: str = '0.0.1'
    _class_creation_date: str = Time.now()
    _class_deletion_date: str = "nan"
    _class_creation_path: Path = Path().cwd()
    _class_working_path: Path = Path.cwd()
    _class_rnd_id: int = randint(0, 1000)

    def __init__(self, **kwargs):
        safe_init_meta_class(self, kwargs)
