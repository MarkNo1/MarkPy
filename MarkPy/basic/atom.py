import time
from dataclasses import dataclass

from .time import datetime

_atom_ = {'class': 'Atom', 'version': 3}


@dataclass
class ClassDetails:
    version: int = 1
    creation_date: datetime = datetime()
    destruction_date: datetime = None


@dataclass
class InheritHistory:
    atoms = {_atom_['class']: ClassDetails(version=_atom_['version'])}

    def add(self, name, version):
        self.atoms[name] = ClassDetails(version)

    def get(self, name):
        return self.atoms[name]

    def show(self):
        return str(self.atoms)


class Atom:

    def __init__(self, name, version):
        if not hasattr(self, '_history'):
            self._history = InheritHistory()
            self._history.add(name=name, version=version)
        else:
            self._history.add(name=name, version=version)

    def _get_atom_inherit_history(self):
        return self._history

    def _get_atom_inherit_class(self, name):
        return self._history.get(name)

    def _show_inherit_history(self):
        return self._history.show()

    def __hash__(self):
        return hash(self._history)
