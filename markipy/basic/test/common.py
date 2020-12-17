import unittest
from HtmlTestRunner import HTMLTestRunner
from markipy import DEFAULT_UNITTEST_FOLDER, ensure_folder


def get_unittest_work_log_dirs(component):
    work_dir = DEFAULT_UNITTEST_FOLDER / component
    log_dir = work_dir / 'logs'
    ensure_folder(work_dir)
    ensure_folder(log_dir)
    return work_dir, log_dir
