
def format_list(my_list):
    """ Return a string with the items with an even index in the list, 
    seperated by a comma ana space 
    and the last item in the list with the word 'and' beforehand.
   :param my_list: the list with the items
   :param new_even_list: will get the items in the even spaces of the list
   :param formated_string: will add the space and comma turning the list to a string
   :type my_list: list
   :type new_even_list: list
   :type formated_string: string
   :return: The items in the list as a string with the formatting applied
   :rtype: string
    """
    my_list[-1] = "and " + my_list[-1] #add the and requirement to appear before the last item
    print(my_list, type(my_list))
    new_even_list = my_list[1::2]
    print(new_even_list, type(new_even_list))
    formated_string = ", ".join(new_even_list)
    print(formated_string, type(formated_string))     
    #last_item = my_list.pop()
    #my_list.insert(0,last_item)
    return(formated_string)

the_list = input("Enter items to place in a list: ")
the_list = the_list.split()
print(the_list)
shifted_list = format_list(the_list)
print("Here is the formated list: ",shifted_list, type(shifted_list))


