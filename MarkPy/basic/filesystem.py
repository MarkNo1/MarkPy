from .logger import Logger


from os import makedirs, remove
from shutil import rmtree
from pathlib import Path


# ParentPathCreationNewFileNotFound
class FileParentException(Exception):
    def __init__(self, File):
        File.log.error(f"({self.name}): Parent path not exist of  {File.red(File.__file__)}")


class File(Logger):

    __file_version__ = 1

    def __init__(self, fileName, path=Path.cwd()):
        Logger.__init__(self, fileName)
        self.newLogAtom('File', self.__file_version__)
        self.__file__ = Path(path) / fileName
        init_opt = self.orange('attached')

        if not Path(path).exists():
            raise FileParentException(self)

        if not self.__file__.exists():
            init_opt = self.green('created')
            with open(self.__file__, 'w') as fd:
                fd.write('')

        self.initialized()
        self.log.debug(f' File {init_opt} -> {self.violet(self.__file__)}')


class LogFolder():

    def __log_folder_created__(self):
        self.log().debug(f"folder {self.__folder__} created by: {self.__name__}")

    def __log_folder_usedby__(self):
        self.log().debug(f"folder {self.__folder__} used by: {self.__name__}")

    def __log_list_folders__(self):
        self.log().debug("call list_folder")

    def __log_list_files__(self):
        self.log().debug("call list_files")

    def __log_delete_folder__(self, target):
        self.log().debug(f"call delete_folder on:\t{target}")

    def __log__delete_file__(self, target):
        self.log().debug(f"call delete_file on:\t{target}")

    def __log__empty_folder__(self):
        self.log().debug("call empty_folder")




class InitializationFolder(Logger, LogFolder):
    def __init__(self, folder=None):
        self.__folder__ = Path(folder) if folder else Path.cwd()
        if not self.__folder__.exists():
            makedirs(self.__folder__, exist_ok=True)
        Logger.__init__(self, f'Folder.{self.__folder__}', self.__folder__.parent / f'{folder}.logs')
        LogFolder.__init__(self)
        self.__log_folder_created__()



class Folder(InitializationFolder):

    def list_folders(self):
        self.__log_list_folders__()
        return [x for x in  self.__folder__.iterdir() if x.is_dir()]

    def list_files(self):
        self.__log_list_files__()
        return [x for x in  self.__folder__.iterdir() if x.is_file()]

    def delete_folder(self, target=None):
        if target is None:
            target = self.__folder__
        self.__log_delete_folder__(target)
        rmtree(target)

    def delete_file(self, target):
        self.__log__delete_file__(target)
        remove(target)

    def empty_folder(self):
        self.__log__empty_folder__()
        for folder in self.list_folders():
            self.delete_folder(folder)
        for file in self.list_files():
            self.delete_file(file)


def test_file():
    file = File("test_file")



def test_folder():
    folder = Folder("test_folder")
    folder.list_files()
    folder.list_folders()
    folder.delete_folder()
