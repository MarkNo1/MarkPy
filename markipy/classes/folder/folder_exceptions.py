class FolderException:
    class AttachToFile(Exception):
        def __init__(self, cls):
            cls.log.error(f"Folder cannot be attached to a file: {cls.red(cls._folder_path)}")
