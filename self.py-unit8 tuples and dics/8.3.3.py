
def note():
    """
    >>> magic_str = "abra cadabra"
    >>> count_chars(magic_str)
    {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
    """

def count_chars(my_str):
    """get a string in a param and return a dic were every char in the string
     (not space) is a key and the times it appears in the string is the value
    """

    the_key_list = find_keys(my_str)
    print("looked at the string. this is the key list i created:", the_key_list)
    chars_dic = {}  
    i = 0
    while i < len(the_key_list):
        chars_dic[the_key_list[i]] = find_appearance(the_key_list[i], my_str)
        i += 1
    
    return chars_dic

def find_keys(my_str):
    key_list = []
    for char in my_str:
        if char not in key_list and char != " ":
            key_list.append(char)
    return key_list

def find_appearance(key, my_str):
    appearance_number = my_str.count(key)
    return appearance_number 

magic_str = "aviel zwebner"
print(count_chars(magic_str))