import yaml
import unittest

from dataclasses import dataclass
from markipy.entities.base import Configuration
from markipy.entities.base import Path

working_dir = Path().cwd()

test_0_params = dict(
    _class_name='Configuration',
    _class_working_path=working_dir,
    _class_log_path=working_dir / 'log',
    _class_cfg_path=working_dir / 'cfg'
)

test_1_params = dict(_class_cfg_path=working_dir / 'cfg')


class TestConfiguration(unittest.TestCase):

    def test_initialization_0_from_params(self):
        cfg = Configuration(**test_0_params)
        self.assertEqual(cfg._class_name, 'Configuration')

    def test_initialization_1_from_cfg(self):
        cfg = Configuration(**test_1_params)

        with open(cfg._cfg_file_path, 'r') as cf:
            cfg_ = yaml.safe_load(cf)

        self.assertEqual(cfg._class_name, 'Configuration')
        self.assertEqual(cfg._cfg_sync, cfg_['_cfg_sync'])
        self.assertEqual(cfg._class_cfg_path, cfg_['_class_cfg_path'])
        self.assertEqual(cfg._class_deletion_date, cfg_['_class_deletion_date'])
        self.assertEqual(cfg._class_log_path, cfg_['_class_log_path'])
        self.assertEqual(cfg._class_rnd_id, cfg_['_class_rnd_id'])
        self.assertEqual(cfg._class_version, cfg_['_class_version'])
        self.assertEqual(cfg._class_working_path, cfg_['_class_working_path'])

    @dataclass(unsafe_hash=True, init=False)
    class ChildConfiguration(Configuration):
        param1: int = 28
        param2: str = "Test"

    def test_initialization_0_from_params_child(self):
        cfg = self.ChildConfiguration(**test_0_params)
        self.assertEqual(cfg._class_name, 'ChildConfiguration')

    def test_initialization_1_from_cfg_child(self):
        cfg = self.ChildConfiguration(**test_1_params)

        with open(cfg._cfg_file_path, 'r') as cf:
            cfg_ = yaml.safe_load(cf)

        self.assertEqual(cfg._class_name, 'ChildConfiguration')
        self.assertEqual(cfg.param1, cfg_['param1'])
        self.assertEqual(cfg.param2, cfg_['param2'])

    @dataclass(unsafe_hash=True, init=False)
    class NestedConfiguration(Configuration):
        class1: Configuration = Configuration(**test_1_params)
        class2: Configuration = Configuration(**test_1_params)

    def test_initialization_0_from_params_factory(self):
        cfg = self.NestedConfiguration(**test_0_params)
        self.assertEqual(cfg._class_name, 'NestedConfiguration')

    def test_initialization_1_from_params_factory(self):
        cfg = self.NestedConfiguration(**test_0_params)
        cfg1 = Configuration(**cfg.class1)
        cfg2 = Configuration(**cfg.class2)

        with open(cfg1._cfg_file_path, 'r') as cf:
            cfg_ = yaml.safe_load(cf)

        self.assertEqual(cfg._class_name, 'NestedConfiguration')

        self.assertEqual(cfg1._class_name, 'Configuration')
        self.assertEqual(cfg1._cfg_sync, cfg_['_cfg_sync'])
        self.assertEqual(cfg1._class_cfg_path, cfg_['_class_cfg_path'])
        self.assertEqual(cfg1._class_deletion_date, cfg_['_class_deletion_date'])
        self.assertEqual(cfg1._class_log_path, cfg_['_class_log_path'])
        self.assertEqual(cfg1._class_rnd_id, cfg_['_class_rnd_id'])
        self.assertEqual(cfg1._class_version, cfg_['_class_version'])
        self.assertEqual(cfg1._class_working_path, cfg_['_class_working_path'])

        self.assertEqual(cfg2._class_name, 'Configuration')
        self.assertEqual(cfg2._cfg_sync, cfg_['_cfg_sync'])
        self.assertEqual(cfg2._class_cfg_path, cfg_['_class_cfg_path'])
        self.assertEqual(cfg2._class_deletion_date, cfg_['_class_deletion_date'])
        self.assertEqual(cfg2._class_log_path, cfg_['_class_log_path'])
        self.assertEqual(cfg2._class_rnd_id, cfg_['_class_rnd_id'])
        self.assertEqual(cfg2._class_version, cfg_['_class_version'])
        self.assertEqual(cfg2._class_working_path, cfg_['_class_working_path'])


if __name__ == '__main__':
    unittest.main()
