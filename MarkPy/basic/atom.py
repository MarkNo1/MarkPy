import time
from dataclasses import dataclass

from .time import datetime

_atom_ = {'name': 'Atom', 'version': '2'}


class Atom:
    _name = _atom_['name']
    _version = _atom_['version']
    _create_date: str = datetime()

    _names = []
    _versions = []

    def __init__(self, atom='Atom', version=_atom_['version']):
        self._names += [atom]
        self._versions += [version]

    def getName(self):
        return self._name

    def getStrNames(self):
        return '>'.join(self._names)

    def getStrVersions(self):
        return '>'.join(self._versions)

    def getVersion(self):
        return self.version

    def getNames(self):
        return self._names

    def getVersions(self):
        return self._versions

    def getAtomCreateDate(self):
        return self._create_date

    def __hash__(self):
        return hash(self.getStrNames() + self.getStrVersions())
