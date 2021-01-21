from dataclasses import dataclass, fields
from markipy import makedirs
import yaml
from . import Path, Time, Color, Emoji

META_TAG = '@do.'


def split_by_tag(text, tag=META_TAG):
    if tag in text:
        return text.split(tag)[1]


@dataclass(unsafe_hash=True, init=False)
class Meta:
    _name: str = 'BaseMeta'
    _version: str = '4.0.3'

    _sync: bool = True
    _date_create: str = '@do.self.Time.now()'
    _date_delete: str = "nan"
    _date_sync: str = '@do.self.Time.now()'
    _path: Path = '@do.self.Path.cwd()'

    _path_cfg: Path = '@do.self._path / "cfg" / f"{self._name}.cfg"'
    _path_bp: Path = '@do.self._path / "bp" / f"{self._name}.bp"'
    _path_ini_log: Path = '@do.self._path / "log" / f"{self._name}.ini"'
    _path_log: Path = '@do.self._path / "log" / f"{self._name}.log"'

    _log_mode: str = 'console'
    _id: str = '@do.f"{self._name}_{hash(self)}"'

    Path: Path = Path
    Time: Time = Time
    Color: Color = Color
    Emoji: Emoji = Emoji

    def __init__(self, **kwargs):
        self._safe_init_(kwargs)

        if not Path(self._path).exists():
            makedirs(self._path, exist_ok=True)

        if not self._path_cfg.parent.exists():
            makedirs(self._path_cfg.parent, exist_ok=True)

        if not self._path_bp.parent.exists():
            makedirs(self._path_bp.parent, exist_ok=True)

        if not Path(self._path_log).exists():
            makedirs(self._path_log.parent, exist_ok=True)

            # Sync Enable
        if self._sync:
            self.cfg_dump()

    def _safe_init_(self, kwargs):
        fields_name = set([f.name for f in fields(self)])

        for field in fields(self):
            if type(field.default) is str:
                if META_TAG in field.default and field.name not in kwargs:
                    kwargs.update({field.name: field.default})

        for k, v in kwargs.items():
            if k in fields_name:
                if type(v) is str and META_TAG in v:
                    setattr(self, k, eval(split_by_tag(v)))
                else:
                    setattr(self, k, v)

        setattr(self, '_name', self.__class__.__name__)

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

    def get_path(self):
        return self._path

    def cfg_dump(self):
        self._date_sync = Time.now()
        self._cfg_dump()
        self._blueprint_dump()

    def _cfg_dump(self):
        with open(str(self._path_cfg), 'w') as cf:
            yaml.dump(self.to_dict(), cf, default_flow_style=False)

    def _blueprint_dump(self):
        with open(str(self._path_bp), 'w') as cf:
            yaml.dump(self.to_blueprint(), cf, default_flow_style=False)

    # def cfg_load(self) -> dict:
    #     with open(str(self.get_path_bp()), 'r') as f:
    #         g = yaml.safe_load(f)
    #         cfg = g.copy()
    #         # Filtering if start and end with _ Private Init in  the CLass
    #         for k, v in g.items():
    #             if k[0] == '_' and k[-1] == '_':
    #                 cfg.pop(k, None)
    #         return cfg

    def __del__(self):
        self._date_delete = Time.now()
        if self._sync:
            self.cfg_dump()
