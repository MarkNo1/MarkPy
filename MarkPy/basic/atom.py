from .time import datetime

__atom_version__ = 2

class Atom:
    def __init__(self, name, type):
        self.__name__ = name
        self.__type__ = type
        self.__create_date__ = datetime()
        self.__version__ = __atom_version__

    def newAtom(self, name, version):
        self.__name__ += f'.{name}'
        self.__version__ = f'{version}.{self.__version__}'
