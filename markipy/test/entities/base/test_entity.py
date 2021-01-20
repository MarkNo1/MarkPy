# import unittest
# from dataclasses import dataclass
# from time import sleep
# from markipy.entities.base import Path
# from markipy.entities import Entity
#
# working_dir = Path().cwd()
#
# test_0_params = dict(
#     _class_name='Entity',
#     _class_working_path=working_dir,
#     _class_log_path=working_dir / 'log',
#     _class_cfg_path=working_dir / 'cfg',
#     _log_mode_=Entity.LoggerMode.file
# )
#
# test_1_params = dict(_class_cfg_path=working_dir / 'cfg', _log_mode_=Entity.LoggerMode.file)
#
#
# class TestLoggerClass(unittest.TestCase):
#
#     def test_entity_init(self):
#         e = Entity(**test_0_params)
#         e.log.debug('test_entity_init')
#         sleep(0.1)
#         del e
#
#     @dataclass(unsafe_hash=True, init=False)
#     class TestEntity(Entity):
#         param1: int = 28
#
#     def test_entity_load(self):
#         e = self.TestEntity(**test_1_params)
#         e.log.debug('test_entity_load')
#         sleep(1)
#         del e
