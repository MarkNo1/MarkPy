from MarkPy.erectus import time_ns, pwd, path, isFile


class Path(object):
    def __init__(self, filename, folder):
        super().__init__()
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
    def __init__(self, filename, folder):
        if __debug__:
            print(f'File {filename} - Ini')
        Path.__init__(self, filename, folder)

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
    counter = Incremental()

    def __init__(self, Name):
        if __debug__:
            print(f'State {Name} - Ini')
        File.__init__(self, Name, pwd())
        self.Cicle = -1
        self.Time = time_ns()
        self.Action = 'Born'
        self.Status = 'Initialization'
        self.Name = Name


    def init_state(self):
        self.state = self.state

    def getter(self):
        if __debug__:
            print(f'State {self.Name} - Get')
        return [self.Time, self.Cicle, self.Action, self.Status]

    def setter(self, state):
        if __debug__:
            print(f'State {self.Name} - Set')

        assert isinstance(state, list) and  2 < len(state) < 5 , f"CheckStateInpute: {state}"
        self.update(state)

    def deleter(self):
        if __debug__:
            print(f'State {self.Name} - Del')

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

    def state_to_str(self,state):
        return ' , '.join([str(t) for t in state]) + '\n'

    def __str__(self):
        return f'State {self.Name}: {self.Time}, {self.Cicle}, {self.Action}, {self.Status}\n'

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
            print(f'Logger {Name} - Ini')
        State.__init__(self, Name)
        self.Name = Name
        self.statelog = self.statelog


    def getter(self):
        if __debug__:
            print(f'Logger {self.Name} - Get')
        return self.state

    def setter(self, state):
        if __debug__:
            print(f'Logger {self.Name} - Set')
        self.state = state
        self.file = self.state_to_str(self.state)

    def deleter(self):
        if __debug__:
            print(f'Logger {self.Name} - Del')

    statelog = property(getter,setter,deleter, 'StateLogger Quartz')






class Property(Logger):
    '''
        Version v0.0.1                                           (TM)
        ______________

        Arguments:
        __________

    '''

    def __init__(self,  Name='Default', Value=None):
        if __debug__:
            print(f'Property{Name} - Ini')
        Logger.__init__(self, Name)
        self.Value = Value
        self.Name = Name

    def __get__(self, Instance, Owner):
        if __debug__:
            print(f'Property{self.Name} - Get')
        self.statelog = [ 0, 'Get', self.Value]
        return self.Value

    def __set__(self, Instance, Value):
        if __debug__:
            print(f'Property{self.Name} - Set')

        self.Value = Value
        self.statelog = [ 0, 'Set', self.Value]


    def __del__(self):
        if __debug__:
            print(f'Property{self.Name} - Del')

    def __str__(self):
        return f'Property: {self.Name}'
