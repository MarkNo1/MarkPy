from MarkPy.habilis import ClassDictionaryCommon
from MarkPy.habilis import InputError

class PropertySetPropertiesError(InputError):
    '''
        Check that the value passed by args or kwargs is a dictionary.
    '''

    def __init__(self):
        self.message = 'Check that the value passed by args or kwargs is a dictionary.'



class Property(ClassDictionaryCommon):
    def __init__(self):
        super(ClassDictionaryCommon, self).__init__('properties', 'property')


    def get_property(self, name):
        return self.properties[name]

    def set_properties(self, *args, **kwargs):
        check_args = len(args)
        check_kwargs = len(kwargs)
        if check_args > 0:
            self.add_to_property(args)
        if check_kwargs > 0:
            self.add_to_property(kwards)
        if  check_args == check_kwargs == 0:
            raise PropertySetPropertiesError()

    def set_property(self, name, property):
        self.properties[name] = property

    def add_to_property(self, dictionary):
        if not self.dict_empty(dictionary):
            self.properties.update(dictionary)
