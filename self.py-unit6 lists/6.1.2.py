

def shift_left(my_list):
    """Shift items in the list to the left.
   :param my_list: the list with the items
   :param last_item: will get the last item from my list
   :type my_list: list
   :type last_item: string
   :return: The list with the items shifted to the left
   :rtype: list
    """
    last_item = my_list.pop()
    my_list.insert(0,last_item)
    return(my_list)

the_list = input("Enter items to place in a list: ")
the_list = the_list.split()
print(the_list)
shifted_list = shift_left(the_list)
print("I shifted all the items to the lfet: ",shifted_list)


