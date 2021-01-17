from dataclasses import dataclass
import yaml
from .text import TextFile


@dataclass(init=False, unsafe_hash=True)
class YmlFile(TextFile):

    def _file_read(self) -> dict:
        cfg = yaml.safe_load(self._file)
        for k, v in cfg.items():
            # Do command after the @do
            if type(v) is str and '@do' in v:
                cfg[k] = eval(f"{v.split('@do')[1]}")
            # Cast to double
            elif type(v) is str and '1e' in v:
                cfg[k] = eval(f"float({v})")
        return cfg

