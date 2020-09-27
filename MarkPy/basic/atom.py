from .time import datetime

__atom_version__ = 1

class Atom:
    def __init__(self):
        self.__name__ = 'Atom'
        self.__create_date__ = datetime()
        self.__version__ = __atom_version__

    def newAtom(self, atom_name, atom_version):
        self.__name__ += f'.{atom_name}'
        self.__version__ = f'{atom_version}.{self.__version__}'
