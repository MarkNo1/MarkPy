from MarkPy.erectus import time_ns, pwd, path, isFile


class Path(object):
    def __init__(self, filename, folder):
        if __debug__:
            print(f'Path {folder}\{filename} - Ini')
        self.path = path(folder, filename)
        self.filename = filename
        self.folder = folder



class File(Path):
    '''
            Version v0.0.3                                          (TM)
            ______________

                Arguments:
                __________

    '''
    def __init__(self, filename, folder=pwd()):
        if __debug__:
            print(f'File {filename} - Ini')
        super().__init__(filename, folder)

    def getter(self):
        if __debug__:
            print(f'File {self.filename} - Get')
        with open(self.path, 'r+') as fd:
            return fd.read()

    def setter(self, Text):
        if __debug__:
            print(f'File {self.filename} - Set')
        with open(self.path, 'a+') as fd:
            return fd.write(str(Text))

    def deleter(self):
        if __debug__:
            print(f'File {self.filename} - Del')

    file = property(getter,setter,deleter, 'File Quartz')



class Incremental(object):
    '''
        Version v0.0.1                                           (TM)
        ______________

            Arguments:
            __________

    '''

    def __init__(self, InitVal=0):
        self.index = InitVal

    def __get__(self, obj, objtype):
        self.index += 1
        return self.index -1

    def __set__(self, obj, index):
        self.index = index



class State(File):
    '''
        Version v0.0.1                                           (TM)
        ______________

            Arguments:
            __________

    '''

    def __init__(self, Name):
        if __debug__:
            print('State - Ini')
        super().__init__(Name)
        self.Cicle = Cicle
        self.Time = Time
        self.Action = Action
        self.Status = Status
        self.counter = Incremental()

    def getter(self):
        if __debug__:
            print('State - Get')
        return [self.Time, self.Cicle, self.Action, self.Status]

    def setter(self, state):
        if __debug__:
            print('State - Set')

        assert isinstance(state, list) and  2 < len(state) < 5 , f"CheckStateInpute: {state}"
        self.update(state)

    def deleter(self):
        if __debug__:
            print('State - Del')

        del self.Time
        del self.Cicle
        del self.Status
        del self.Action

    def update(self, NewState):
        self.counter = 0
        if len(NewState) == 4:
            self.Time = NewState[self.counter]
        else:
             self.Time = time_ns()

        self.Cicle = NewState[self.counter]
        self.Status = NewState[self.counter]
        self.Action = NewState[self.counter]


    def __str__(self):
        return f'State: {self.Time}, {self.Cicle}, {self.Action}, {self.Status}\n'

    state = property(getter,setter,deleter, 'State Quartz')


class Logger(State):
    '''
        Version v0.0.1                                           (TM)
        ______________

            Arguments:
            __________

    '''
    def __init__(self, Name, folder=pwd()):
        if __debug__:
            print('StateLogger - Ini')
        super(State, self).__init__(Name)

        self.state = [-1, 'Init', 'Created']


    def getter(self):
        if __debug__:
            print('StateLogger - Get')
        return self.state

    def setter(self, state):
        if __debug__:
            print('StateLogger - Set')
        self.state = state
        self.file = str(self.state)

    def deleter(self):
        if __debug__:
            print('StateLogger - Del')

    statelog = property(getter,setter,deleter, 'StateLogger Quartz')






class Property(Logger):
    '''
        Version v0.0.1                                           (TM)
        ______________

        Arguments:
        __________

    '''

    def __init__(self,  Name='Default', Value=None):
        super().__init__(Name)
        if __debug__:
            print('Property - Ini')
        self.Value = Value
        self.Name = Name

    def __get__(self, Instance, Owner):
        if __debug__:
            print('Property - Get')
        self.statelog = [ 0, 'Get', self.Value]
        return self.Value

    def __set__(self, Instance, Value):
        if __debug__:
            print('Property - Set')

        self.Value = Value
        self.statelog = [ 0, 'Set', self.Value]


    def __del__(self):
        if __debug__:
            print('Property - Del')

    def __str__(self):
        return f'Property: {self.Name}'
