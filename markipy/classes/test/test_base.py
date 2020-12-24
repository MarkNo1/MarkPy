from markipy.classes import BaseClass
from markipy.classes.test import unittest


class TestBaseClass(unittest.TestCase):

    def test_initialization_no_params(self):
        base = BaseClass()
        self.assertEqual(base._class_deletion_date, 'nan')
        self.assertEqual(base._class_name, 'BaseMeta')
        self.assertEqual(base._class_version, '0.0.1')

    def test_initialization_with_params(self):
        base = BaseClass(_class_name='BaseClass', _class_version='0.0.0')
        self.assertEqual(base._class_name, 'BaseClass')
        self.assertEqual(base._class_version, '0.0.0')
        self.assertEqual(base._class_deletion_date, 'nan')

    def test_multiple_initialization_with_params(self):
        base1 = BaseClass(_class_name='BaseClass1', _class_version='0.0.1')
        base2 = BaseClass(_class_name='BaseClass2', _class_version='0.0.2')
        self.assertEqual(base1._class_name, 'BaseClass1')
        self.assertEqual(base1._class_version, '0.0.1')
        self.assertEqual(base1._class_deletion_date, 'nan')

        self.assertEqual(base2._class_name, 'BaseClass2')
        self.assertEqual(base2._class_version, '0.0.2')
        self.assertEqual(base2._class_deletion_date, 'nan')

    def test_hashes(self):
        base1 = BaseClass(_class_name='BaseClass1', _class_version='0.0.1')
        hash(base1)


if __name__ == '__main__':
    unittest.main()
