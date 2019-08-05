from MarkPy.habilis import ClassDictionaryCommon
from MarkPy.habilis import InputError

class ModifierArgIsNotADictionaryError(InputError):
    ''' Exception for bad input into the modifiers '''
    def __init__(*args):
        self.args = args

class ModifierInputIsEmpty(InputError):
    ''' Exception for bad input into the modifiers '''
    def __init__(*args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class Modifier(ClassDictionaryCommon):
    def __init__(self):
        super(DictionaryCommon, self).__init__()
        self.ensure_attribute('_modifiers_')


    def get_modifier(self, modifier):
        return self.get_attribute('_modifiers_')

    def set_modifiers(self, *args, **kwargs):
        input = self.check_inputs(args, kwargs)


    def set_modifier(self, name, property):
        self._modifiers_[name] = property

    def set_modifier_from_dict(self, dictionary):
        if not isinstance(dictionary, dict):
            raise ModifierArgIsNotADictionaryError(dictionary)

        for modifier_name, modifier in dictionary.items():
            self.set_modifier(modifier_name, modifier)
