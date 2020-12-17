import yaml

from .filesystem import File


def do_load(cfg):
    raw = yaml.safe_load(cfg)

    for k, v in raw.items():
        # Do command after the @do
        if type(v) is str and '@do' in v:
            raw[k] = eval(f"{v.split('@do')[1]}")
        # Cast to double
        elif type(v) is str and '1e' in v:
            raw[k] = eval(f"float({v})")

    return raw


class Yaml(File):

    def load(self, do=False):
        if self.exist():
            if not do:
                with open(self.__file__, 'r') as fd:
                    return yaml.safe_load(fd)
            else:
                with open(self.__file__, 'r') as fd:
                    return do_load(fd)
        else:
            return None
