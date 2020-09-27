from MarkPy.time import datetime


class Atom:
    def __init__(self, name, type):
        self.__name__ = name
        self.__type__ = type
        self.__create_date__ = datetime()
