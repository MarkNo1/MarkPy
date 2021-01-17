# from markipy.classes.test import unittest
# from time import sleep
# from markipy.classes.path import Path
# from markipy.classes.watcher import Watcher
# from markipy.classes.file import TextFile
#
#
# ws = dict(_class_working_path=Path('/tmp/unittest/'), _watcher_path=Path('/tmp/unittest/'))
# file_name = 'Test-Watcher-File.info'
#
#
# class ExampleWatcher(Watcher):
#     _last_event = None
#
#     def __init__(self, **kwargs):
#         Watcher.__init__(self, **kwargs)
#
#     def event_file_moved(self, event):
#         print(event)
#         self._last_event = event
#
#     def event_file_modified(self, event):
#         print(event)
#         self._last_event = event
#
#     def event_file_created(self, event):
#         print(event)
#         self._last_event = event
#
#     def event_file_deleted(self, event):
#         print(event)
#         self._last_event = event
#
#     def event_dir_moved(self, event):
#         print(event)
#         self._last_event = event
#
#     def event_dir_modified(self, event):
#         print(event)
#         self._last_event = event
#
#     def event_dir_created(self, event):
#         print(event)
#         self._last_event = event
#
#     def event_dir_deleted(self, event):
#         print(event)
#         self._last_event = event
#
#     def get_last_event(self):
#         return self._last_event
#
#
# class TestWatcher(unittest.TestCase):
#
#     def test_watcher_base(self):
#         w = ExampleWatcher(**ws)
#         self.assertEqual(w._class_name, 'ExampleWatcher')
#         self.assertEqual(w._watcher_path, Path('/tmp/unittest/'))
#         w.stop()
#         w.join()
#
#     def test_watcher_events(self):
#         w = ExampleWatcher(**ws)
#         w.start()
#         ft = TextFile(**ws, _file_name=file_name, _file_mode=TextFile.FileMode.write)
#         ft.open()
#         ft.close()
#         print(w.get_last_event())
#         w.stop()
#         w.join()
#
#     # def test_watcher_communication_events(self):
#     #     mq = MessageQueue()
#     #     w = WatcherEventProducer(**ws, **mq.share_logger(), _watcher_com_channel=mq)
#     #     w.start()
#     #     sleep(0.5)
#     #     ft = TextFile(**ws, _file_name=file_name, _file_mode=TextFile.FileMode.write)
#     #     ft.open()
#     #     ft.close()
#     #     while not w._watcher_com_channel.is_buffer_empty():
#     #         print(w._watcher_com_channel.receive())
#     #     del w
#
#
# if __name__ == '__main__':
#     unittest.main()
