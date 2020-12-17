from .common import unittest, get_unittest_work_log_dirs

from markipy.basic.yml import Yaml

WRK_DIR, LOG_DIR = get_unittest_work_log_dirs('yaml')


YAML_CFG_TEST = '''
name: to-init
val_1: 1
val_2: 2.0
val_3: 1e0
val_4: 1e0 * 4
val_5: [5]
val_6: "@do hash('a6')"
val_7: "@do dict(hash=hash('b7'))"
'''


def compare(a, b):
    res = a == b
    if res:
        return True
    else:
        print(f"[error-comparison]: {a} == {b}")
    return


def compare_target_config(cfg):
    if compare(cfg['name'], 'to-init') and \
            compare(cfg['val_1'], 1) and \
            compare(cfg['val_2'], 2.0) and \
            compare(cfg['val_3'], 1e0) and \
            compare(cfg['val_4'], 1e0 * 4) and \
            compare(cfg['val_5'], [5]) and \
            compare(cfg['val_6'], hash('a6')) and \
            compare(cfg['val_7']['hash'], hash('b7')):
        return True
    else:
        return False


class TestYaml(unittest.TestCase):

    def test_load_configuration_from_file(self):
        target_file = WRK_DIR / 'unittest-yaml.yml'

        file = Yaml(target_file)
        file.write(YAML_CFG_TEST)

        yml = Yaml(target_file, log_path=LOG_DIR)
        cfg = yml.load(do=True)
        self.assertEqual(compare_target_config(cfg), True)

    def test_load_configuration_from_variable(self):
        target_file = WRK_DIR / 'unittest-yaml-variable.yml'

        yml = Yaml(target_file, log_path=LOG_DIR)
        cfg = yml.load_from_variable(YAML_CFG_TEST, do=True)
        self.assertEqual(compare_target_config(cfg), True)


if __name__ == '__main__':
    unittest.main()
