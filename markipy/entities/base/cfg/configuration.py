from dataclasses import dataclass
import yaml

from markipy import makedirs
from ..meta import Meta
from ..path import Path
from ..time import Time


@dataclass(init=False, unsafe_hash=True)
class Configuration(Meta):
    _meta_name: str = 'Configuration'

    _cfg_sync: bool = True
    _cfg_sync_date: str = '@do.self.Time.now()'
    _cfg_filename: str = 'Configuration'

    _cfg_path: Path = '@do.self._meta_cwd_path / "cfg"'
    _bp_path: Path = '@do.self._meta_cwd_path / "bp"'


    def cfg_load(self) -> dict:
        with open(str(self.get_bp_path()), 'r') as f:
            g = yaml.safe_load(f)
            cfg = g.copy()
            # Filtering if start and end with _ Private Init in  the CLass
            for k, v in g.items():
                if k[0] == '_' and k[-1] == '_':
                    cfg.pop(k, None)
            return cfg

    def cfg_dump(self):
        self._cfg_sync_date = Time.now()
        self._cfg_dump()
        self._cfg_blueprint_dump()

    def _cfg_dump(self):
        with open(str(self.get_cfg_path()), 'w') as cf:
            yaml.dump(self.to_dict(), cf, default_flow_style=False)

    def _cfg_blueprint_dump(self):
        with open(str(self.get_bp_path()), 'w') as cf:
            yaml.dump(self.to_blueprint(), cf, default_flow_style=False)

    def __init__(self, **kwargs):
        Meta.__init__(self, **kwargs)

        self._safe_init_(kwargs)

        if not self._cfg_path.exists():
            makedirs(self._cfg_path, exist_ok=True)

        if not self._bp_path.exists():
            makedirs(self._bp_path, exist_ok=True)

        # Sync Cfg Enable
        if self._cfg_sync:
            self.cfg_dump()

    def get_cfg_path(self):
        return self._cfg_path / f'{self._cfg_filename}.cfg'

    def get_bp_path(self):
        return self._bp_path / f'{self._cfg_filename}.bp'
