from .common import unittest

from markipy.basic.yml import do_load

YAML_CFG_TEST = '''
name: to-init
val_1: 1
val_2: 2.0
val_3: 1e1
val_4: 1e1 * 4
val_5: [5]
val_6: "@do hash('a6')"
val_7: "@do dict(b7=hash('b7'))"
'''


class TestCollection(unittest.TestCase):

    def test_load_configuration(self):
        cfg = do_load(YAML_CFG_TEST)
        print(cfg)
