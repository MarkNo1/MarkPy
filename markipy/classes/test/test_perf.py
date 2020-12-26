from markipy.classes.test import unittest

from markipy.classes.path import Path
from markipy.classes.perf import Perf
from markipy.classes.time import Time

ws = dict(_class_working_path=Path('/tmp/unittest/'))


class TestPerf(unittest.TestCase):
    class ChildPerf(Perf):
        def __init__(self, **kwargs):
            Perf.__init__(self, **kwargs)

        @Perf.performance
        def test_method(self):
            Time.sleep(1)

    def test_file_text_initialization(self):
        cp = self.ChildPerf()
        cp.test_method()
        cp.test_method()
        print(cp._perf_statistics)


if __name__ == '__main__':
    unittest.main()
