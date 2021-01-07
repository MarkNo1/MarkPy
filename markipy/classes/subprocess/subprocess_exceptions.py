class SubProcessException:
    class EmptyCommandPassed(Exception):
        def __init__(self, cls):
            cls.log.error(f"Empty command: {cls.red(cls._process_cmd)}")
