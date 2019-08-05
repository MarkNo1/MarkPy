from MarkPy.habilis.property import Property
from MarkPy.erectus.filesystem import pwd, path

PROPERTY_1 = 'born_path'
PROPERTY_2 = 'current_path'

class PathProperty(Property):
    def __init__(self, specialization):
        super(Property, self).__init__()
        self.set_properties(**{ PROPERTY_1:pwd(), PROPERTY_2:pwd() });

    def get_born_path(self):
        return self.get_property(PROPERTY_1)

    def get_current_path(self):
        return self.get_property(PROPERTY_2)

    def set_current_path(self, path):
        self.set_property(PROPERTY_2 , path)
