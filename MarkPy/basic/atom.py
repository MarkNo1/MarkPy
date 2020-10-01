import time
from dataclasses import dataclass

from .time import datetime


_atom_version = '1'


@dataclass
class Atom:

    _name : str = 'Atom'
    _create_date : str = datetime()
    _version : str = _atom_version

    def newAtom(self, atom_name, atom_version):
        self._name += f'>{atom_name}'
        self._version += f'.{atom_version}'

    def getAtomName(self):
        return self._name

    def getAtomVersione(self):
        return self._version

    def getAtomCreateDate(self):
        return self._create_date
