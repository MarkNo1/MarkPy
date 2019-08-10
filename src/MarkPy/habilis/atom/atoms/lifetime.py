from MarkPy.habilis.atom import Atom
from MarkPy.erectus.time import time


class TimeAtom(Atom):
    def __init__(self, Name= 'TimeAtom'):
        super(Atom, self).__init__(Name)
        self._borntime = time()

    @property
    def borntime(self):
        return self._borntime

    @borntime.setter
    def borntime(self, Reset=time()):
        self._borntime = Reset
