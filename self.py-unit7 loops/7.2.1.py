
#>>> result = is_greater([1, 30, 25, 60, 27, 28], 28)
#>>> print(result)
#[30, 60]

def is_greater(my_list, n):
    """ get a list and a number
    return a new list with all the items larger than the given number.
   :param my_list: a list of numbers
   :param n: number to be the condition if larger than
   :type my_list: list of int
   :type n: int
   :return: new list of numbers meeting the condition
   :rtype: list
    """
    collect_results = []
    for item in my_list:
        #print(item)
        if int(item) > n:
            collect_results.append(item)
    return(collect_results)

numbers_list = (input("Enter numbers for the list: "))
numbers_list = numbers_list.split()
number = int(input("Enter a number to be the starting value for the new list: "))
new_list = is_greater(numbers_list, number)
print(numbers_list, "\n", new_list)


