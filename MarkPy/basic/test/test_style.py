import unittest

from MarkPy.basic import Atom


class Child(Atom):
    def __init__(self):
        Atom.__init__(self, 'Child', 1)


class Nephew(Child):
    def __init__(self):
        Child.__init__(self)
        Atom.__init__(self, 'Nephew', 2)


class TestAtom(unittest.TestCase):

    def test_atom_creation(self):
        a = Atom('Test', 1)
        self.assertEqual(a._get_atom_inherit_class('Atom').version, 1)
        self.assertEqual(a._get_atom_inherit_class('Test').version, 1)
        del a

    def test_atom_inheritance(self):
        c = Child()
        self.assertEqual(c._get_atom_inherit_class('Atom').version, 1)
        self.assertEqual(c._get_atom_inherit_class('Child').version, 1)

    def test_atom_multiple_inheritance(self):
        n = Nephew()
        self.assertEqual(n._get_atom_inherit_class('Atom').version, 1)
        self.assertEqual(n._get_atom_inherit_class('Child').version, 1)
        self.assertEqual(n._get_atom_inherit_class('Nephew').version, 2)


if __name__ == '__main__':
    unittest.main()
