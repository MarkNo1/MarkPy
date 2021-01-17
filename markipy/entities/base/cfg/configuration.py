from dataclasses import dataclass
import yaml

from markipy import makedirs, _cfg_default_dir

from ..class_meta import ClassMeta
from ..path import Path
from ..time import Time


@dataclass(init=False, unsafe_hash=True)
class Configuration(ClassMeta):
    _class_cfg_path: Path = _cfg_default_dir

    _cfg_sync: bool = True
    _cfg_sync_date: str = 'nan'
    _cfg_file_path: Path = None

    def cfg_load(self) -> dict:
        with open(self._cfg_file_path, 'r') as cf:
            cfg = yaml.safe_load(cf)
            for k, v in cfg.items():
                # Text type
                if type(v):
                    # Set creation date
                    if 'creation_date' in k:
                        cfg[k] = Time.now()
                    # Do command after the @do
                    if '@do' in v:
                        cfg[k] = eval(f"{v.split('@do')[1]}")
                    # Cast to double
                    elif '1e' in v:
                        cfg[k] = eval(f"float({v})")

            return cfg

    def cfg_dump(self):
        self._cfg_sync_date = Time.now()
        with open(self._cfg_file_path, 'w') as cf:
            yaml.dump(self.to_dict(), cf, default_flow_style=False)

    def __init__(self, **kwargs):
        ClassMeta.__init__(self, **kwargs)

        # Configuration Path to init
        if self._cfg_file_path is None:
            if not Path(self._class_cfg_path).exists():
                makedirs(self._class_cfg_path, exist_ok=True)
            self._cfg_file_path = Path(self._class_cfg_path) / Path(f'{self._class_name}.yml')

        else:
            # Exist but is str type
            if type(self._cfg_file_path) is str:
                self._cfg_file_path = Path(self._cfg_file_path)

        # Sync Cfg Enable
        if self._cfg_sync:
            # If configuration file exist
            if self._cfg_file_path.exists():
                # Load params from cfg
                cfg = self.cfg_load()
                self._safe_init_(cfg)
            else:
                # Load params from kwargs
                self._safe_init_(kwargs)
                # Register current cfg
                self.cfg_dump()
