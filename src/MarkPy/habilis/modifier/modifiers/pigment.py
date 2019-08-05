from MarkPy.habilis.modifier import Modifier
from MarkPy.erectus.style import Colorize


'''

    PIGMENT

'''

MODIFIER = 'pigment'


class Pigment(object):
    def __init__(self, color_id):
        self._color_id_ = color_id

    def __call__(self, element):
        return Colorize(self._color_id_, element)


class PigmentModifier(Modifier):
    def __init__(self, *args, **kwargs):
        super(Modifier, self).__init__()
        self.set_pigment(args, kwargs)

    def get_pigment(self, name):
        return self.get_modifier([MODIFIER])

    def set_pigments(self, *args, **kwargs):
        if self.check_args_sanity(args):
            self.set_modifier_from_dict(args)
        elif self.check_kwargs_sanity(kwargs):
            self.set_modifier_from_dict(args)
        else:
            raise ModifierInputIsEmpty(args,kwargs)

        self.set_modifiers(args,kwargs)

    def set_pigment(self, name, color_id):
        self.get_modifier(MODIFIER)[name] = Pigment(color_id)
        self._set_pigment_call_(name)

    def _set_pigment_call_(self, name):
        self.__dict__['get_pigment_' + name] = lambda name : self.get_pigment(name)
