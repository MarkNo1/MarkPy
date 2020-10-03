import unittest

from MarkPy.basic import Atom


class TestAtom(unittest.TestCase):

    def test_attributes(self):
        a = Atom('Test', 1)
        self.assertEqual(a.getName() == 'Test')
        self.assertEqual(a.getVersion() == 1)


if __name__ == '__main__':
    unittest.main()