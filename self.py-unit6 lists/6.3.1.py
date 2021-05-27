
def are_lists_equal(list1, list2):
    """ Receive two lists with only float or int items. the function return true only if both lists hold exactly the same items regardless of the order.
   :param list_1: the first list with the items
   :param list_2: the second list
   :type list_1: list of int or float
   :type list_2: list of int or float
   :return: true or false 
   :rtype: boolean
    """
    
    result = False
    if len(list1) == len(list2): 
        list1.sort()
        list2.sort()
        print(list1, list2)
        list1 = [ int(x) for x in list1 ] #convert items from string to int
        list2 = [ int(x) for x in list2 ] #need to add a check that all items in list are numbers and can be converted to int otherwise can get error
        print(list1, list2)
        if list1 == list2:
            result = True
    #else: result = False
    return(result)

list_one = input("Enter items to place in List One: ")
list_two = input("Enter items to place in List Two: ")
list_one = list_one.split()
list_two = list_two.split()
print(list_one, type(list_one), list_two, type(list_two))
check_lists = are_lists_equal(list_one, list_two)
print("The lists hold the same items: ", check_lists)


