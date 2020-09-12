from MarkPy.erectus import time_ns
from MarkPy.habilis.common.exception_utils import InputError


class PropertySetPropertiesError(InputError):
    '''
        Check that the value passed by args or kwargs is a dictionary.
    '''

    def __init__(self):
        self.message = 'Check that the value passed by args or kwargs is a dictionary.'





class Property(object):
    '''
        Version v0.0.1                                           (TM)
        ______________

        Arguments:
        __________

            *args           Collection of element.
                            Initially as *args was expected only string.
    '''

    def __init__(self,  Name='Default', Value=None):
        self.Value = Value
        self.Name = Name
        self.History = []

    def __get__(self, Obj, ObjType):
        self.update('Get')
        return self.Value

    def __set__(self, Obj, Value):
        self.update('Set')
        self.Value = Value

    def update(self, Message):
        print('History', self.History)
        self.History.append([time_ns(), Message])




class State(object):
    def __init__(self, Time=time_ns(), Action='None', Status=None):
        self.Time = Time
        self.Action = Action
        self.Status = Status

    def __get__(self, obj, objtype):
        return [self.Time, self.Status, self.Action]

    def __set__(self, obj, state):
        assert isinstance(state, list) and  1 <= len(state) <= 4 , "CheckStateInpute"
        self.update(state)


    def update(self, NewState):
        index = Index()
        if len(NewState) == 2:
            self.Time = time_ns()

        self.Status = state[index]
        self.Action = state[index]




class Index(object):
    def __init__(self, Start=0):
         self.I = Start
    def __get__(self, obj, objtype):
         self.I +=1
         return self.Value -1
    def __set__(self, obj, index):
         self.I = index


# class Property(ClassDictionaryCommon):
#     def __init__(self):
#         super(ClassDictionaryCommon, self).__init__('properties', 'property')
#
#
#     def get_property(self, name):
#         return self.properties[name]
#
#     def set_properties(self, *args, **kwargs):
#         check_args = len(args)
#         check_kwargs = len(kwargs)
#         if check_args > 0:
#             self.add_to_property(args)
#         if check_kwargs > 0:
#             self.add_to_property(kwards)
#         if  check_args == check_kwargs == 0:
#             raise PropertySetPropertiesError()
#
#     def set_property(self, name, property):
#         self.properties[name] = property
#
#     def add_to_property(self, dictionary):
#         if not self.dict_empty(dictionary):
#             self.properties.update(dictionary)
