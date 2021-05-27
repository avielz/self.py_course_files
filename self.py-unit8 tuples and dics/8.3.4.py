

def note():
    """
    >>> course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    >>> inverse_dict(course_dict)
    {3: ['I', 'love'], 2: ['self.py!']}
    """

def inverse_dict(my_dict):
    """get a dic as a param return an inverse dic where all values become keys and vice versa.
    note that this may cause keys that appear more than once so gat the values in the new dict as a list.
    sort values lists
    """

    new_keys_list = get_values(my_dict)

    new_dic = {}  
    i = 0
    while i < len(new_keys_list):
        new_dic[new_keys_list[i]] = get_keys(new_keys_list[i], my_dict)
        i += 1
    
    return new_dic

def get_values(my_dict):
    value_list = []
    for value in my_dict.values():
        if value not in value_list:
            value_list.append(value)
    print("these are the new dic keys:", value_list)
    return value_list  

def get_keys(new_key, my_dict):
    key_list = []
    for key, value in my_dict.items(): 
        if value == new_key:
            key_list.append(key)
    key_list.sort()
    print("these are the matching keys i found:", key_list)
    return key_list  

course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict))
