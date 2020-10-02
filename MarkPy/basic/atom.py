import time
from dataclasses import dataclass

from .time import datetime

_atom_ = {'name': lambda: 'Atom', 'version': lambda: 2}


@dataclass
class Atom:
    _name = _atom_['name']
    _create_date: str = datetime()
    _version = _atom_['version']

    def __init__(self, name, version):
        self._name = name
        self._version = version

    def newAtom(self, atom_name, atom_version):
        self._name += f'>{atom_name}'
        self._version += f'.{atom_version}'

    def getAtomName(self):
        return self._name

    def getAtomVersione(self):
        return self._version

    def getAtomCreateDate(self):
        return self._create_date

    def __hash__(self):
        return hash('1')
