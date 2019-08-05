# Check dictionary is empty
check_if_dictionary = lambda x : True if isinstance(x, dict) else False

def dict_empty(dictionary):
    if not check_if_dictionary(dictionary):
        raise 'Passed not a dictionary to [dict_empty]'
    return  len(dictionary) == 0

def check_key(dictionary):
    if not check_if_dictionary(dictionary):
        raise 'Passed not a dictionary to [dict_empty]'
    return  key in dictionary.keys()
