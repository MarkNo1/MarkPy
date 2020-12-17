from .common import unittest, get_unittest_work_log_dirs

from markipy.basic import Channel

WRK_DIR, LOG_DIR = get_unittest_work_log_dirs('channel')


class TestChannel(unittest.TestCase):

    def test_channel_in_out(self):
        var = [10, 20, 30]
        c = Channel()
        c.put(var)
        var_channel = c.get()
        self.assertEqual(var, var_channel)


if __name__ == '__main__':
    unittest.main()
