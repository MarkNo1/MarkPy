import yaml
import unittest

from dataclasses import dataclass
from markipy.entities.base import Configuration
from markipy.entities.base import Path, Time

working_dir = Path().cwd()

ConfigurationBlueprint = '''\
_cfg_blueprint_path: '@do.Path.cwd() / "bp"'
_cfg_filename: Configuration
_cfg_sync: true
_cfg_sync_date: '@do.Time.now()'
_meta_cfg_path: '@do.Path.cwd() / "cfg"'
_meta_creation_date: '@do.Time.now()'
_meta_cwd_path: '@do.Path.cwd()'
_meta_deletion_date: nan
_meta_log_path: '@do.Path.cwd() / "log"'
_meta_name: Configuration
_meta_rnd_id: '@do.randint(0, 1000)'
_meta_version: 4.0.1
'''

test_0_params = dict(
    _meta_name='Configuration',
    _cfg_sync=True,
    _cfg_filename='Configuration',
    _cfg_save_blueprint=working_dir / 'log',
    _meta_cfg_path=working_dir / 'cfg',
    _cfg_blueprint_path=working_dir / 'cfg'
)

test_1_params = dict(_meta_cfg_path=working_dir / 'cfg')


def get_param_0(name):
    return test_0_params[name]


class TestConfiguration(unittest.TestCase):

    def test_init_0_generation(self):
        cfg = Configuration(**test_0_params)
        self.assertEqual(cfg._meta_name, get_param_0('_meta_name'))

    def test_init_1__smart_load_cfg(self):
        cfg = Configuration(**test_1_params)

    # def test_init_1_load_cfg(self):
    #     cfg = Configuration(**test_1_params)
    #     cfg_ = smart_load_yml(cfg.cfg_bp_path())
    #
    #     self.assertEqual(cfg._meta_name, get_param_0('_meta_name'))
    #     self.assertEqual(cfg._cfg_sync, cfg_['_cfg_sync'])
    #     self.assertEqual(cfg._meta_cfg_path, cfg_['_meta_cfg_path'])
    #     self.assertEqual(cfg._meta_deletion_date, cfg_['_meta_deletion_date'])
    #     self.assertEqual(cfg._meta_log_path, cfg_['_meta_log_path'])
    #     self.assertEqual(cfg._meta_version, cfg_['_meta_version'])
    #     self.assertEqual(cfg._meta_cwd_path, cfg_['_meta_cwd_path'])

    # @dataclass(unsafe_hash=True, init=False)
    # class TestForkConfiguration(Configuration):
    #     param1: int = 28
    #     param2: str = "Test"
    #
    # def test_init_0_generation_forked(self):
    #     cfg = self.TestForkConfiguration(**test_0_params)
    #     self.assertEqual(cfg._meta_name, 'TestForkConfiguration')
    #
    # def test_init_1_forked(self):
    #     cfg = self.TestForkConfiguration(**test_1_params)
    #
    #     cfg_ = smart_load_yml(cfg._cfg_file_path)
    #
    #     self.assertEqual(cfg._meta_name, 'TestForkConfiguration')
    #     self.assertEqual(cfg.param1, cfg_['param1'])
    #     self.assertEqual(cfg.param2, cfg_['param2'])

    # @dataclass(unsafe_hash=True, init=False)
    # class NestedConfiguration(Configuration):
    #     class1: Configuration = Configuration(**test_1_params)
    #     class2: Configuration = Configuration(**test_1_params)
    #
    # def test_initialization_0_from_params_factory(self):
    #     cfg = self.NestedConfiguration(**test_0_params)
    #     self.assertEqual(cfg._meta_name, 'NestedConfiguration')
    #     print(cfg)
    #     print(type(cfg.class1))
    #     print(type(cfg.class2))
    #
    # def test_initialization_1_from_params_factory(self):
    #     cfg = self.NestedConfiguration(**test_0_params)
    #     cfg1 = Configuration(**cfg.class1.to_dict())
    #     cfg2 = Configuration(**cfg.class2.to_dict())
    #
    #     cfg_ = smart_load_yml(cfg._cfg_file_path)
    #
    #     self.assertEqual(cfg._meta_name, 'NestedConfiguration')
    #
    #     self.assertEqual(cfg1._meta_name, 'Configuration')
    #     self.assertEqual(cfg1._cfg_sync, cfg_['_cfg_sync'])
    #     self.assertEqual(cfg1._meta_cfg_path, cfg_['_meta_cfg_path'])
    #     self.assertEqual(cfg1._meta_deletion_date, cfg_['_meta_deletion_date'])
    #     self.assertEqual(cfg1._meta_log_path, cfg_['_meta_log_path'])
    #     self.assertEqual(cfg1._meta_rnd_id, cfg_['_meta_rnd_id'])
    #     self.assertEqual(cfg1._meta_version, cfg_['_meta_version'])
    #     self.assertEqual(cfg1._meta_cwd_path, cfg_['_meta_cwd_path'])
    #
    #     self.assertEqual(cfg2._meta_name, 'Configuration')
    #     self.assertEqual(cfg2._cfg_sync, cfg_['_cfg_sync'])
    #     self.assertEqual(cfg2._meta_cfg_path, cfg_['_meta_cfg_path'])
    #     self.assertEqual(cfg2._meta_deletion_date, cfg_['_meta_deletion_date'])
    #     self.assertEqual(cfg2._meta_log_path, cfg_['_meta_log_path'])
    #     self.assertEqual(cfg2._meta_rnd_id, cfg_['_meta_rnd_id'])
    #     self.assertEqual(cfg2._meta_version, cfg_['_meta_version'])
    #     self.assertEqual(cfg2._meta_cwd_path, cfg_['_meta_cwd_path'])


if __name__ == '__main__':
    unittest.main()
