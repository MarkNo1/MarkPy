from MarkPy.habilis.property import Property

PROPERTY = 'specialization'

class SpecializationProperty(Property):
    def __init__(self, specialization):
        super(Property, self).__init__()
        self.add_properties({ PROPERTY:specialization });
