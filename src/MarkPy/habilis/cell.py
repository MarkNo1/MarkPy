from .pigment import Pigment
from MarkPy.erectus.filesystem import pwd
from MarkPy.erectus.time import time
'''
@ Cell
'''


# Styles
blue = 610
lightblue = 6420
yellow_blue_underline = 9345

'''
    INTERFACE ATOM
'''


class InterfaceCell(object):
    def __init__(self, specialization=''):
        super().__init__()
        self.__pigments__()
        self.__defaults__(specialization)

    def __defaults__(self, specialization):
        self.__specialization__ = specialization
        self.__root__ = pwd()
        self.__born_in__ = time()
        self.__die_in__ = None

    def __pigments__(self):
        self._blue_ = Pigment(blue)
        self._lightblue_ = Pigment(lightblue)
        self._yellow_u_blue = Pigment(yellow_blue_underline)

    def _colorize_(self, style, text):
        return Colorize(style, text)

    def __del__(self):
        self.__die_in__ = time()

    def __repr__(self):
        return f'Cell | {self._blue_(self.__specialization__)} - {self._lightblue_(self.__born_in__)}\n     | {self._yellow_u_blue(self.__root__)}'

    def __str__(self):
        return f'Cell [ {self.__specialization__}, {self.__born_in__}, {self.__root__} ]'


'''
    ATOM
'''


class Cell(InterfaceCell):
    pass
