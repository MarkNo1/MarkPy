from markipy.entities.base import Meta, Time, Path
from markipy import _unittest_default_dir
import unittest
from markipy.entities.base.time import Time

test_default_params = dict(
    _meta_name='Meta',
    _meta_version='4.0.1',
    _meta_cwd_path=_unittest_default_dir,
    _meta_log_path=_unittest_default_dir / 'log',
    _meta_cfg_path=_unittest_default_dir / 'cfg'
)


def get_param(name):
    return test_default_params[name]


class TestMeta(unittest.TestCase):

    def test_init_0_(self):
        base = Meta()
        self.assertEqual(base._meta_name, get_param('_meta_name'))
        self.assertEqual(base._meta_version, get_param('_meta_version'))

    def test_init_1_kwargs(self):
        base = Meta(**test_default_params)

        self.assertEqual(base._meta_name, get_param('_meta_name'))
        self.assertEqual(base._meta_version, get_param('_meta_version'))
        self.assertEqual(base._meta_cwd_path, get_param('_meta_cwd_path'))

    def test_init_2_to_dict(self):
        base = Meta(**test_default_params)
        d = base.to_dict()

    def test_init_3_to_blueprint(self):
        base = Meta(**test_default_params)

        self.assertEqual(base._meta_name, get_param('_meta_name'))
        self.assertEqual(base._meta_version, get_param('_meta_version'))
        self.assertEqual(base._meta_cwd_path, _unittest_default_dir)

    def test_init_3_to_inject_blueprint(self):
        d = Meta(**Meta(**test_default_params).to_blueprint())

        self.assertEqual(d._meta_name, get_param('_meta_name'))
        self.assertEqual(d._meta_version, get_param('_meta_version'))
        self.assertEqual(d._meta_deletion_date, 'nan')
        self.assertEqual(d._meta_cwd_path, Path.cwd())

    def test_init_2_multiple_with_params(self):
        base1 = Meta(_meta_name=get_param('_meta_name'), _meta_version=get_param('_meta_version'))
        base2 = Meta(_meta_name=get_param('_meta_name'), _meta_version=get_param('_meta_version'))
        self.assertEqual(base1._meta_name, get_param('_meta_name'))
        self.assertEqual(base1._meta_version, get_param('_meta_version'))
        self.assertEqual(base1._meta_deletion_date, 'nan')
        self.assertEqual(base2._meta_name, get_param('_meta_name'))
        self.assertEqual(base2._meta_version, get_param('_meta_version'))
        self.assertEqual(base2._meta_deletion_date, 'nan')
        self.assertNotEqual(base1, base2)

    def test_hashes(self):
        base1 = Meta()
        hash(base1)


if __name__ == '__main__':
    unittest.main()
