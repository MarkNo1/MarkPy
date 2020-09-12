# Check dictionary is empty
notDictionary = lambda x : False if isinstance(x, dict) else True

def dict_empty(dictionary):
    if notDictionary(dictionary):
        raise 'Passed not a dictionary to [dict_empty]'
    return  len(dictionary) == 0

def check_key(dictionary):
    if notDictionary(dictionary):
        raise 'Passed not a dictionary to [dict_empty]'
    return  key in dictionary.keys()
