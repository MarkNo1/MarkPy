from MarkPy.habilis.common.exception_utils import InputError
from MarkPy.habilis.common.dictionary import DictionaryCommon


class ClassDictionaryCommon(DictionaryCommon):

    def has_attribute(self, attribute):
        return hasattr(self, attribute)

    def ensure_attribute(self, attribute, element):
        if not self.has_attribute(attribute):
            self.add_attribute(attribute, element)

    def add_attribute(self, name, element):
        self.__dict__[name] = element

    def get_attribute(self, attribute):
        return self.__dict__[attribute]
