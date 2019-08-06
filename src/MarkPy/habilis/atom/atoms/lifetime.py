from MarkPy.habilis.atom import Atom
from MarkPy.erectus.time import time

PROPERTY_1 = 'born_in'
PROPERTY_2 = 'die_in'

# BROKEN - To-DO Fixs
class TimeAtom(Atom):
    def __init__(self, specialization):
        super(Property, self).__init__()
        self.set_properties({ 'born_in': time(), 'die_in': None});

    def get_born_time(self):
        return self.get_property('born_in')

    def get_die_time(self):
        return self.get_property('die_in')

    def set_die_time(self):
        self.set_property('die_in', time())

    def __del__(self):
        self.set_die_time()
