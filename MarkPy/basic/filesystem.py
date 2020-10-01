from .logger import Logger


import os
from shutil import rmtree
from pathlib import Path


# ParentPathCreationNewFileNotFound
class ParentPathException(Exception):
    def __init__(self, File):
        File.log.error(f"({self.name}): Parent path not exist of  {File.red(File.__file__)}")


class File(Logger):

    __file_version__ = 1

    def __init__(self, filePath):
        Logger.__init__(self, f'.file.{Path(filePath).name}')
        self.newLogAtom('File', self.__file_version__)

        self.__file__ = Path(filePath)
        opt_file = self.orange('looking')

        if not self.__file__.parent.exists():
            raise ParentPathException(self)

        if not self.__file__.exists():
            opt_file = self.green('new')
            with open(self.__file__, 'w') as fd:
                fd.write('')

        self.log.debug(self.ugrey(f'Initialized'))
        self.log.debug(f' File {opt_file} -> {self.violet(self.__file__)}')

    def folder(self):
        return self.__file__.parent

    def __str__(self):
        return str(self.__file__).strip()

    def __del__(self):
        Logger.__del__(self)


class Folder(Logger):

    __folder_version__ = 1

    def __init__(self, folderPath='./'):
        Logger.__init__(self, f'.folder.{folderPath}')
        self.newLogAtom('Folder', self.__folder_version__)

        self.__folder__ = Path(folderPath)

        opt_folder = self.orange('looking')
        if not self.__folder__.parent.exists():
            raise ParentPathException(self)

        if not self.__folder__.exists():
            os.makedirs(self.__folder__, exist_ok=False)
            opt_folder =  self.green('new')

        self.log.debug(self.ugrey(f'Initialized'))
        self.log.debug(f' Folder {opt_folder} -> {self.lightviolet(self.__folder__)}')

    def folders(self):
        self.log.debug("call list_folder")
        return [x for x in  self.__folder__.iterdir() if x.is_dir()]

    def files(self):
        self.log.debug("call list_files")
        return [x for x in  self.__folder__.iterdir() if x.is_file()]

    def delete(self, target=None):
        if target is None:
            target = self.__folder__
        self.log.debug(f"call delete_folder on:\t{target}")
        rmtree(target)

    def remove(self, target):
        self.log.debug(f"call delete_file on:\t{target}")
        os.remove(target)

    def empty_folder(self):
        self.log.debug("call empty_folder")
        for folder in self.list_folders():
            self.delete_folder(folder)
        for file in self.list_files():
            self.delete_file(file)

    def __del__(self):
        Logger.__del__(self)


def test_file():
    file = File("test_file")



def test_folder():
    folder = Folder("test_folder")
    folder.files()
    folder.folders()
    folder.delete()
