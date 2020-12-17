from .common import unittest, get_unittest_work_log_dirs

from time import sleep

from markipy.basic import File
from markipy.basic import Watcher

WRK_DIR, LOG_DIR = get_unittest_work_log_dirs('watcher')

_watcher_child_ = {'class': 'WatcherChild', 'version': 1}
_watcher_nephew_ = {'class': 'WatcherNephew', 'version': 1}


class WatcherChild(Watcher):
    def __init__(self, path=WRK_DIR / 'watcher_child_test'):
        Watcher.__init__(self, console=False, path=path, log_path=LOG_DIR)
        self._init_atom_register_class(_watcher_child_)
        self.file_has_created = False
        self.file_has_modified = False

    def task_file_created(self, event):
        self.file_has_created = True

    def task_file_modified(self, event):
        self.file_has_modified = True


class WatcherNephew(WatcherChild):
    def __init__(self, path=WRK_DIR / 'watcher_nephew_test'):
        WatcherChild.__init__(self, path=path)
        self._init_atom_register_class(_watcher_nephew_)


class TestWatcher(unittest.TestCase):

    def test_file_created_watcher(self):
        File(WRK_DIR / 'file_to_watch').remove()
        wf = WatcherChild(WRK_DIR / 'file_to_watch')
        wf.start()

        File(WRK_DIR / 'file_to_watch').write('Init')
        sleep(0.01)

        self.assertEqual(True, wf.file_has_created)

    def test_file_modified_watcher(self):
        wf = WatcherChild(WRK_DIR / 'file_to_watch')
        wf.start()

        File(WRK_DIR / 'file_to_watch').append('Modified')
        sleep(0.01)

        self.assertEqual(True, wf.file_has_modified)

    def test_folder_watcher(self):
        pass


if __name__ == '__main__':
    unittest.main()
