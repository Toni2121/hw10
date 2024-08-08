def remove_key_from_dict(dictionary: dict):
    dictionary.popitem()
def clear_all(dictionary: dict):
    dictionary = {}
    a = {'x': 1, 'y': 2}
    remove_key_from_dict(a)
    print(a)
    clear_all(a)
    print(a)


# The dict that was sent to the function will not remain the same because
# The popitem() method removes the last item from the dictionary

# The dict that was sent to the function will remain the same because
# dictionary is reassigned to a new empty dictionary {} and its only affects the local refernce.


def clear_all(dictionary: dict):
    dictionary.clear()

a = {'x': 1, 'y': 2}
remove_key_from_dict(a)
print(a)
clear_all(a)
print(a)
