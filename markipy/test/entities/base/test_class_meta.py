from markipy.entities.base import ClassMeta
from markipy import _unittest_default_dir
import unittest

test_default_params = dict(
    _class_name='ClassMeta',
    _class_version='0.0.0',
    _class_working_path=_unittest_default_dir,
    _class_log_path=_unittest_default_dir / 'log',
    _class_cfg_path=_unittest_default_dir / 'cfg'
)


class TestClassMeta(unittest.TestCase):

    def test_initialization_no_params(self):
        base = ClassMeta()
        self.assertEqual(base._class_deletion_date, 'nan')
        self.assertEqual(base._class_name, 'ClassMeta')
        self.assertEqual(base._class_version, '0.0.1')

    def test_initialization_with_params(self):
        base = ClassMeta(**test_default_params)
        self.assertEqual(base._class_name, 'ClassMeta')
        self.assertEqual(base._class_version, '0.0.0')
        self.assertEqual(base._class_deletion_date, 'nan')
        self.assertEqual(base._class_log_path, _unittest_default_dir / 'log', )
        self.assertEqual(base._class_cfg_path, _unittest_default_dir / 'cfg')

    def test_multiple_initialization_with_params(self):
        base1 = ClassMeta(_class_name='ClassMeta', _class_version='0.0.1')
        base2 = ClassMeta(_class_name='ClassMeta', _class_version='0.0.2')
        self.assertEqual(base1._class_name, 'ClassMeta')
        self.assertEqual(base1._class_version, '0.0.1')
        self.assertEqual(base1._class_deletion_date, 'nan')

        self.assertEqual(base2._class_name, 'ClassMeta')
        self.assertEqual(base2._class_version, '0.0.2')
        self.assertEqual(base2._class_deletion_date, 'nan')

        self.assertNotEqual(base1, base2)

    def test_hashes(self):
        base1 = ClassMeta(_class_name='ClassMeta1', _class_version='0.0.1')
        hash(base1)


if __name__ == '__main__':
    unittest.main()
