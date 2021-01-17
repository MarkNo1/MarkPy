import unittest
from dataclasses import dataclass

from markipy.classes.path import Path
from markipy.classes.perf import Performance
from markipy.classes.logger import Logger

from markipy.classes.time import Time

ws = dict(_class_working_path=Path('/tmp/unittest/'))


class ChildPerf(Performance):
    def __init__(self, **kwargs):
        Performance.__init__(self, **kwargs)
        
    @Performance.collect_perf
    def test_method(self):
        pass

    @Performance.collect_perf
    def measure_spawn(self):
        pass

    @Performance.collect_perf
    def measure_kill(self):
        pass


TEST_PERF_INSTANCE = ChildPerf(**ws)


@dataclass(init=False, unsafe_hash=True)
class TestPerf(unittest.TestCase):

    Logger = Logger()

    def test_performance_collect(self):
        TEST_PERF_INSTANCE.test_method()
        TEST_PERF_INSTANCE.test_method()
        TEST_PERF_INSTANCE.test_method()
        self.assertAlmostEqual(TEST_PERF_INSTANCE._perf_get_stats_with_name('test_method').min, 200, delta=5e2)
        self.assertAlmostEqual(TEST_PERF_INSTANCE._perf_get_stats_with_name('test_method').max, 200, delta=5e2)
        self.assertAlmostEqual(TEST_PERF_INSTANCE._perf_get_stats_with_name('test_method').mean, 200, delta=5e2)
        self.assertEqual(TEST_PERF_INSTANCE._perf_get_stats_with_name('test_method').count, 3)

    def test_performance_life_dead_measure(self):
        TEST_PERF_INSTANCE.measure_spawn()
        TEST_PERF_INSTANCE.measure_kill()
        self.assertAlmostEqual(TEST_PERF_INSTANCE._perf_get_stats_with_name('measure_spawn').mean, 500, delta=5e2)
        self.assertAlmostEqual(TEST_PERF_INSTANCE._perf_get_stats_with_name('measure_kill').mean, 500, delta=5e2)
        print(TEST_PERF_INSTANCE._perf_get_stats_with_name('measure_spawn'))
        print(TEST_PERF_INSTANCE._perf_get_stats_with_name('measure_kill'))


if __name__ == '__main__':
    unittest.main()
