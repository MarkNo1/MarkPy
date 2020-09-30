from pathlib import Path


def correct_path(input):
    '''
        If the path is in the current dir will return the absolute path
    '''
    return str(Path(input)).strip()
