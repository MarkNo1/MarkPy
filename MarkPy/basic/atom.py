import time
from dataclasses import dataclass

from .time import datetime, clock

_atom_ = {'class': 'Atom', 'version': 3}


class ClassDetails:
    def __init__(self, version):
        self.version = version
        self.creation_date = datetime()
        self.creation_time = clock()
        self.destruction_date: datetime = None

    def __eq__(self, other):
        return self.version == other.version and self.creation_date == other.creation_date and self.creation_time == other.creation_time

    def __hash__(self):
        return hash(self.version)


class InheritHistory:

    def __init__(self, name, version):
        self.atoms = {name: ClassDetails(version=version)}

    def __eq__(self, other):
        return self.atoms == other.atoms

    def __hash__(self):
        _hashes = []
        for atom in self.atoms:
            _hashes += [hash((atom, self.atoms[atom]))]
        return hash(tuple(_hashes))

    def add(self, name, version):
        self.atoms[name] = ClassDetails(version)

    def get(self, name):
        return self.atoms[name]

    def show(self):
        return str(self.atoms)

    def classes(self):
        return list(self.atoms.keys())

    def versions(self):
        return [v.version for k, v in self.atoms.items()]


class Atom:

    def __init__(self, name, version):
        if not hasattr(self, '_history'):
            self._history = InheritHistory(name=_atom_['class'], version=_atom_['version'])
            self._history.add(name=name, version=version)
        else:
            self._history.add(name=name, version=version)

    def _get_atom_inherit_history(self):
        return self._history

    def _get_atom_inherit_class(self, name):
        return self._history.get(name)

    def _get_atom_inherit_classes(self):
        return self._history.classes()

    def _get_atom_inherit_versions(self):
        return self._history.versions()

    def _get_atom_inherit_classes_logs(self):
        return '>'.join(self._get_atom_inherit_classes())

    def _get_atom_inherit_versions_logs(self):
        return '.'.join([str(v) for v in self._get_atom_inherit_versions()])

    def _show_inherit_history(self):
        return self._history.show()

    def _get_class_hash(self):
        return hash(self._history)

    def __hash__(self):
        return hash(self._history)
