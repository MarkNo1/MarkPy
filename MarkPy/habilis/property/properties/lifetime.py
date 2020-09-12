from MarkPy.habilis.property import Property
from MarkPy.erectus.time import time

PROPERTY_1 = 'born_in'
PROPERTY_2 = 'die_in'


class LifeTimeProperty(Property):
    def __init__(self, specialization):
        super(Property, self).__init__()
        self.set_properties({ PROPERTY_1: time(), PROPERTY_2: None});

    def get_born_time(self):
        return self.get_property(PROPERTY_1)

    def get_die_time(self):
        return self.get_property(PROPERTY_2)

    def set_die_time(self):
        self.set_property(PROPERTY_2, time())

    def __del__(self):
        self.set_die_time()
