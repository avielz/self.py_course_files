
def extend_list_x(list_x, list_y):
    """ Get two lists, add the second list to the begining of the first list.
   :param list_x: the first list with the items
   :param list_y: the second list
   :type list_x: list
   :type list_y: list
   :return: list x with the items of list y added to the begining
   :rtype: list
    """
    print("before:",list_x[:1])
    list_x[:0] = list_y #slicing and adding before the 0 item in the list
    return(list_x)

list_one = input("Enter items to place in List One: ")
list_two = input("Enter items to place in List Two: ")
list_one = list_one.split()
list_two = list_two.split()
print(list_one, list_two)
extended_list = extend_list_x(list_one, list_two)
print("Here is the extended list: ", extended_list, type(extended_list))


