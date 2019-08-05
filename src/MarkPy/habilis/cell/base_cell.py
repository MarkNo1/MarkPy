from MarkPy.habilis.property import SpecializationProperty, LifeTimeProperty, PathProperty
from MarkPy.habilis.modifier import PigmentModifier
from MarkPy.erectus.filesystem import pwd
from MarkPy.erectus.time import time

'''
@ Cell Base
'''


# Styles
styles = dict(blue = 610,
              lightblue = 6420,
              yellow_u_blue = 9345)


class CellBase(SpecializationProperty, LifeTimeProperty, PathProperty, PigmentModifier):
    def __init__(self, specialization):
        super(SpecializationProperty, self).__init__(specialization)
        super(LifeTimeProperty, self).__init__()
        super(PathProperty, self).__init__()
        super(PigmentModifier, self).__init__(styles)


    def __repr__(self):
        return f'Cell | {self.get_pigment_blue(self.__specialization__)} \
        - {self.get_pigment_lightblue(self.__born_in__)}\n     \
        | {self.get_pigment_yellow_u_blue(self.__root__)}'

    def __str__(self):
        return f'Cell [ {self.__specialization__},\
                {self.get_born_path}, {self.__root__} ]'
