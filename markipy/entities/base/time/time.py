from time import gmtime, strftime, time_ns, sleep


class Time:
    @staticmethod
    def now():
        return strftime('%Y.%m.%d.%H.%M.%S', gmtime())

    @staticmethod
    def now_ns():
        return time_ns()

    @staticmethod
    def sleep(secs):
        return sleep(secs)
