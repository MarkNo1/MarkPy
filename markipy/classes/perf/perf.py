from dataclasses import dataclass

from ..time import Time
from .perf_meta import PerformanceMeta, PerfMeasureMeta
from ..logger import has_logger_class


@dataclass(init=False, unsafe_hash=True)
class Performance(PerformanceMeta):
    def __init__(self, **kwargs):
        PerformanceMeta.__init__(self, **kwargs)

    def _perf_new_measure(self, name, d_time):
        if name not in self._perf_statistics:
            self._perf_statistics[name] = PerfMeasureMeta(min=d_time, mean=d_time, max=d_time, last=d_time)
        else:
            self._perf_statistics[name].update_measure(d_time)

    def _perf_get_stats_with_name(self, name):
        if name in self._perf_statistics:
            return self._perf_statistics[name]
        else:
            return None

    def get_perf_stats(self):
        return self._perf_statistics

    def collect_perf(method):
        def measure(*args, **kw):
            self = args[0]
            ts = Time.now_ns()
            result = method(*args, **kw)
            te = Time.now_ns() - ts
            self._perf_new_measure(method.__name__, te)
            if has_logger_class(self):
                self.log.debug(self.grey(str(self._perf_get_stats_with_name(method.__name__))))
            return result

        return measure
