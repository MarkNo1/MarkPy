class Profiler(object):
    '''
        Version v0.0.1                                           (TM)
        ______________

        Arguments:
        __________

            *args           Collection of element.
                            Initially as *args was expected only string.
    '''

    def __init__(self):
        import cProfile


    def __call__(self, *args):
        cProfile.run( f'{args[0]}({ ",".join([ args[i] for i in range(1 , len(args) )])})')
