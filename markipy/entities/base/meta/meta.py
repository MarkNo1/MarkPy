import sys
from dataclasses import dataclass, fields
from random import randint
from markipy import makedirs
from ..path import Path
from ..time import Time

META_TAG = '@do.'


def update_kwargs_param_if_needed(kwargs, new_kwargs):
    for k, v in new_kwargs.items():
        if k not in kwargs:
            kwargs.update({k: v})
    return kwargs


def split_by_tag(text, tag=META_TAG):
    if tag in text:
        return text.split(tag)[1]


@dataclass(unsafe_hash=True, init=False)
class Meta:
    _meta_name: str = 'BaseMeta'
    _meta_version: str = '4.0.1'

    _meta_creation_date: str = '@do.self.Time.now()'
    _meta_deletion_date: str = "nan"

    _meta_cwd_path: Path = '@do.self.Path.cwd()'

    _meta_rid: int = '@do.self._meta_get_rid(0, 1000)'

    Path: Path = Path
    Time: Time = Time

    _meta_get_rid = randint

    def __init__(self, **kwargs):
        self._safe_init_(kwargs)

        if not Path(self._meta_cwd_path).exists():
            makedirs(self._meta_cwd_path, exist_ok=True)

    def __del__(self):
        self._meta_deletion_date = Time.now()

    def _safe_init_(self, kwargs):
        class_varname_list = set([f.name for f in fields(self)])

        for field in fields(self):
            if type(field.default) is str:
                if META_TAG in field.default and field.name not in kwargs:
                    kwargs.update({field.name: field.default})

        for k, v in kwargs.items():
            if k in class_varname_list:
                if type(v) is str and META_TAG in v:
                    setattr(self, k, eval(split_by_tag(v)))
                else:
                    setattr(self, k, v)

        setattr(self, '_meta_name', self.__class__.__name__)

    def to_dict(self) -> dict:
        dict_fields = {}
        for field in fields(self):
            if field.type in [bool, int, float]:
                dict_fields[field.name] = getattr(self, field.name)

            elif hasattr(getattr(self, field.name), 'to_dict') and getattr(self, field.name) is not None:
                dict_fields[field.name] = getattr(self, field.name).to_dict()
            else:
                dict_fields[field.name] = str(getattr(self, field.name))
        return dict_fields

    def to_blueprint(self):
        dict_fields = {}
        for field in fields(self):
            dict_fields[field.name] = field.default
        return dict_fields
