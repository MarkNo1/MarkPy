import cProfile
import timeit

class Profiler(object):
    '''
        Version v0.0.1                                           (TM)
        ______________

        Arguments:
        __________

            *args           Collection of element.
                            Initially as *args was expected only string.
    '''

    def __call__(self, *args):
        return cProfile.run(str(args))


    def functionsCalls(self, code= 'p = Profiler()'):
        return self.__call__(code)

    def timeit(self, code='p = Profiler()', number=10, setup='pass'):
        return timeit.timeit(code, number=number, setup=setup)
