import sys
import inspect

from markipy import DEFAULT_UNITTEST_FOLDER
from markipy.basic.test import *


def load_test(test_class):
    return unittest.TestLoader().loadTestsFromTestCase(test_class)


def extract_test_classes():
    _classes = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            if 'markipy' in str(obj):
                _class = str(obj).split('.')[-1]
                _class = _class.replace(">", "").replace("'", "")
                _classes.append(eval(f"load_test({_class})"))
    return _classes


# Add here the test to be perform
def registered_test_suite():
    return unittest.TestSuite(extract_test_classes())


def unittest_markipy():
    HTMLTestRunner(output=DEFAULT_UNITTEST_FOLDER, combine_reports=True).run(registered_test_suite())


if __name__ == '__main__':
    unittest_markipy()
