from .common import unittest, get_unittest_work_log_dirs

WRK_DIR, LOG_DIR = get_unittest_work_log_dirs('collection')


class TestCollection(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
