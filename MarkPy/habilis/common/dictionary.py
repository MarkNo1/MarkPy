from MarkPy.erectus.dictionary import dict_empty, check_key
from .exception_utils import InputError

class DictionaryEmptyConsideredAsError(InputError):
    def __init__(self, name):
        self.name = name


class DictionaryCommon(object):
    def dict_empty(self, dictionary):
        return dict_empty(dictionary)

    def check_key(self, dictionary):
        return check_key(dictionary)
