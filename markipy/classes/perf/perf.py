from dataclasses import dataclass, field
import time

from ..time import Time
from .perf_meta import PerfMeta, PerfMetaMeasure


@dataclass(init=False, unsafe_hash=True)
class Perf(PerfMeta):
    def __init__(self, **kwargs):
        PerfMeta.__init__(self, **kwargs)

    def _perf_new_measure(self, name, d_time):
        if name not in self._perf_statistics:
            self._perf_statistics[name] = PerfMetaMeasure(min=d_time, mean=d_time, max=d_time, last=d_time)
        else:
            self._perf_statistics[name].update_measure(d_time)

    def _perf_get_method_stats(self, name):
        return str(self._perf_statistics[name])

    def performance(method):
        def measure(*args, **kw):
            self = args[0]
            ts = Time.now_ns()
            result = method(*args, **kw)
            self._perf_new_measure(method.__name__, Time.now_ns() - ts)
            if hasattr(self, 'log'):
                self.log.debug(self.grey(self._perf_get_method_stats(method.__name__)))
            return result

        return measure
