from dataclasses import dataclass
import yaml
from ..file import File


def do_load_yaml(cfg):
    raw = yaml.safe_load(cfg)
    for k, v in raw.items():
        # Do command after the @do
        if type(v) is str and '@do' in v:
            raw[k] = eval(f"{v.split('@do')[1]}")
        # Cast to double
        elif type(v) is str and '1e' in v:
            raw[k] = eval(f"float({v})")
    return raw


@dataclass(init=False, unsafe_hash=True)
class YamlFile(File):

    _class_name = 'YamlFile'

    def _file_attach_init(self) -> bool:
        return True

    def _file_open(self) -> bool:
        self._file = open(self._file_path, self._file_mode.value)
        return True

    def _file_read(self) -> dict:
        return do_load_yaml(self._file)

    def _file_write(self, text: str):
        self._file.write(str(text))
        return True

    def _file_close(self) -> bool:
        self._file.close()
        return True
