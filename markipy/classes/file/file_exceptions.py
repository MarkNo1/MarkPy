class FileException:
    class AttachToFolder(Exception):
        def __init__(self, cls):
            cls.log.error(f"File cannot be attached to a folder: {cls.red(cls._file_path)}")

    class AttachError(Exception):
        def __init__(self, cls):
            cls.log.error(f"File cannot be attached to: {cls.red(cls._file_path)}")

    class OpenError(Exception):
        def __init__(self, cls):
            cls.log.error(f"File cannot be opened to: {cls.red(cls._file_path)}")

    class CloseError(Exception):
        def __init__(self, cls):
            cls.log.error(f"File cannot be closed to: {cls.red(cls._file_path)}")

    class WriteModeNotEnabled(Exception):
        def __init__(self, cls):
            cls.log.error(f"File cannot be modified: {cls.red(cls._file_path)}")

    class ReadModeNotEnabled(Exception):
        def __init__(self, cls):
            cls.log.error(f"File cannot be read: {cls.red(cls._file_path)}")