from time import gmtime, strftime


class Time:
    @staticmethod
    def now():
        return strftime('%Y.%m.%d.%H.%M.%S', gmtime())
