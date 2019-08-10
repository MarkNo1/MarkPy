from MarkPy.erectus import time_ns, pwd, path, isFile

class Property(object):
    '''
        Version v0.0.1                                           (TM)
        ______________

        Arguments:
        __________

    '''

    def __init__(self,  Name='Default', Value=None):
        if __debug__:
            print('Property - Ini')

        self.Value = Value
        self.Name = Name
        self.Logger = Logger(Name)

    def __get__(self, Instance, Owner):
        if __debug__:
            print('Property - Get')

        self.Logger = State(Action='Get',Status=self.Value)
        return self.Value

    def __set__(self, Instance, Value):
        if __debug__:
            print('Property - Set')

        self.Logger = State(Action='Set',Status=self.Value)

    def __del__(self):
        if __debug__:
            print('Property - Del')

        del self.Logger



class State(object):
    '''
        Version v0.0.1                                           (TM)
        ______________

            Arguments:
            __________

    '''

    def __init__(self, Time=time_ns(), Action='None', Status=None):
        if __debug__:
            print('State - Ini')
        self.Time = Time
        self.Action = Action
        self.Status = Status
        self.counter = Incremental()

    def __get__(self, Instance, Owner):
        if __debug__:
            print('State - Get')

        return [self.Time, self.Action, self.Status]

    def __set__(self, obj, NewState):
        if __debug__:
            print('State - Set')

        assert isinstance(state, list) and  1 < len(state) < 4 , "CheckStateInpute"
        self.update(state)

    def update(self, NewState):
        if len(NewState) == 2:
            self.Time = time_ns()
        else:
             NewState[self.counter]

        self.Status = NewState[self.counter]
        self.Action = NewState[self.counter]

    def __del__(self, Instance):
        if __debug__:
            print('State - Del')

        del self.Time
        del self.Status
        del self.Action

    def __str__(self):
        return ' , '.join( [ self.Time, self.Action, self.Status ] )




class Logger(object):
    '''
        Version v0.0.1                                           (TM)
        ______________

            Arguments:
            __________

    '''
    def __init__(self, file):
        if __debug__:
            print('Logger - Ini')

        self.__File__ = PFile(file)
        self.__logger__ = PFile('.MPyLog.' + file)
        self.__reader__ = Incremental()
        self.__writer__ = Incremental()

    def __get__(self, Instance, Owner):
        if __debug__:
            print('Logger - Get')

        _ = self.__Counter_Reader__
        return self.__File__

    def __set__(self, Instance, Log):
        if __debug__:
            print('Logger - Set')

        self.__File__ = Log

    def trace(self, mode='G'):
        if mode is 'G':
            readn = self.__reader__
            self.__reader__ = readn
        else:
            writen = self.__writer__
            self.__writer__ = writen

        self.__logger__ =  f'{time_ns()} :\n\tReade : {readn}\t\tWrited : {writed}'

    def __del__(self):
        if __debug__:
            print('Logger - Del')

        del self.__File__
        del self.__logger__
        del self.__reader__
        del self.__writer__


class File(object):
    '''
        Version v0.0.1                                           (TM)
        ______________

            Arguments:
            __________

    '''
    def __init__(self, Name, Folder=pwd()):
        if __debug__:
            print('File - Ini')
        self.Path = self.create(path(Folder, Name))
        self.__Writer__  = open(Path, 'a+')
        self.__Reader__ = open(Path, 'r+')

    def create(self, path):
        if not isFile(path):
            __New__ = open(path, 'x')
            __New__.close()
        return path

    def __get__(self, Instance, Owner):
        if __debug__:
            print('File - Get')

        return self.__Reader__.read()

    def __set__(self, Instance, Text):
        if __debug__:
            print('File - Set')

        self.__Writer__.write(Text)

    def __del__(self):
        if __debug__:
            print('File - Del')

        self.__Writer__.close()
        self.__Reader__.close()


class PFile:
    def __init__(self, Name, Folder=pwd()):
        if __debug__:
            print('File - Ini')
        self.__Writer__  = open(path(Folder, Name), 'a+')
        self.__Reader__ = open(path(Folder, Name), 'r+')

    @property
    def file(self):
        if __debug__:
            print('File - Get')
        return self.__Reader__.read()

    @file.setter
    def file(self, Text):
        if __debug__:
            print('File - Set')
        self.__Writer__.write(Text)

    @file.deleter
    def file(self):
        if __debug__:
            print('File - Del')

        self.__Writer__.close()
        self.__Reader__.close()



class Incremental(object):
    '''
        Version v0.0.1                                           (TM)
        ______________

            Arguments:
            __________

    '''

    def __init__(self, InitVal=0):
        self.index = InitVal

    def __get__(self, Instance, Owner):
        self.index += 1
        return self.index -1

    def __set__(self, Instance, index):
        self.index = index
