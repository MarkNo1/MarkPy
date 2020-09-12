class Importer:
    '''
        Version v0.0.1                                           (TM)
        ______________

        Arguments:
        __________

            Module          Relative Python Package.


            *args           Collection of element.

    '''

    def __init__(self, Module = 'MarkPy'):
        self.module =  __import__(Module)
        self.name = Module

    def __call__(self, *args):
        if len(args) == 1:
            return getattr(self.module, args[0])

        return [getattr(self.module, _class) for _class in [args[i] for i in range(len(args))]]
