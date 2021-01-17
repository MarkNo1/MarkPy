import dataclasses
from random import randint

from ..path import Path
from ..time import Time


def update_kwargs_param_if_needed(kwargs, new_kwargs):
    for k, v in new_kwargs.items():
        if k not in kwargs:
            kwargs.update({k: v})
    return kwargs


@dataclasses.dataclass(unsafe_hash=True, init=False)
class ClassMeta:
    _class_name: str = 'BaseMeta'
    _class_version: str = '0.0.1'

    _class_creation_date: str = Time.now()
    _class_deletion_date: str = "nan"

    _class_cfg_path: Path = Path().cwd()
    _class_log_path: Path = Path().cwd()
    _class_working_path: Path = Path.cwd()

    _class_rnd_id: int = randint(0, 1000)

    def __init__(self, **kwargs):
        self._safe_init_(kwargs)

    def __del__(self):
        self._class_deletion_date = Time.now()

    def _safe_init_(self, kwargs):
        names = set([f.name for f in dataclasses.fields(self)])
        for k, v in kwargs.items():
            if k in names:
                setattr(self, k, v)
        setattr(self, '_class_name', self.__class__.__name__)

    def to_dict(self) -> dict:
        dict_fields = {}
        for field in dataclasses.fields(self):
            if isinstance(getattr(self, field.name), ClassMeta):
                dict_fields[field.name] = getattr(self, field.name).to_dict()
            else:
                dict_fields[field.name] = str(getattr(self, field.name))
        return dict_fields
