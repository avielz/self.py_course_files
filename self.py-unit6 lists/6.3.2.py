
#111 234 2000 goru birthday 09 test values

# A function that returns the length of the value:
def length_check(e):
  return len(e)

def longest(my_list):
    """ Receive a list of strings, returns longest string.
   :param my_list: the  list with the strings
   :param longest_str: the longest string in the list
   :type my_list: list of strings
   :type longest_str: string
   :return: longest string 
   :rtype: string
    """
    my_list.sort(reverse=True, key=length_check)
    print(my_list)
    result = my_list[0]
    return(result)

list_one = input("Enter items to place in List: ")
list_one = list_one.split()
print(list_one, type(list_one))
check_list = longest(list_one)
print("The longest string in the list is: ", check_list)


