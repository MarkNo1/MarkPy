from MarkPy.erectus.style import Colorize


'''

    PIGMENT

'''

default = 8480

class InterfacePigment(object):
    def __init__(self, style=default):
        self.style = style

    def __call__(self, element):
        return Colorize(self.style, element)


class Pigment(InterfacePigment):
    pass
