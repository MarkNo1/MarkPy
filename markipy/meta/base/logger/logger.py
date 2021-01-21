
'''
[loggers]
keys=root,dev

[handlers]
keys=consoleHandler

[formatters]
keys=extend,simple

[logger_root]
level=INFO
handlers=consoleHandler

[logger_dev]
level=INFO
handlers=consoleHandler
qualname=dev
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=INFO
formatter=extend
args=(sys.stdout,)

[formatter_extend]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

[formatter_simple]
format=%(asctime)s - %(message)s
'''

import logging
import logging.config

logging.config.fileConfig(fname='log.conf')

class Logger:
    pass
