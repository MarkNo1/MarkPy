from markipy.classes.test import unittest

from markipy.classes.path import Path
from markipy.classes.perf import Performance
from markipy.classes.time import Time

ws = dict(_class_working_path=Path('/tmp/unittest/'))


class TestPerf(unittest.TestCase):
    class ChildPerf(Performance):
        def __init__(self, **kwargs):
            Performance.__init__(self, **kwargs)

        @Performance.collect_perf
        def test_method(self):
            Time.sleep(1)

    def test_performance_collect(self):
        cp = self.ChildPerf(**ws)
        cp.test_method()
        cp.test_method()
        self.assertAlmostEqual(cp._perf_get_stats_with_name('test_method').min, 1e9, delta=1289902.0)
        self.assertAlmostEqual(cp._perf_get_stats_with_name('test_method').max, 1e9, delta=1289902.0)
        self.assertAlmostEqual(cp._perf_get_stats_with_name('test_method').mean, 1e9, delta=1289902.0)
        self.assertEqual(cp._perf_get_stats_with_name('test_method').count, 2)


if __name__ == '__main__':
    unittest.main()
