from .time import datetime
from .style import Style

class Atom:
    def __init__(self, name, type):
        self.__name__ = name
        self.__type__ = type
        self.__create_date__ = datetime()
        self._style_ = Style()
