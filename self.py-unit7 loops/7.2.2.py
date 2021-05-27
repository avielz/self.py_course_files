#>>> print(numbers_letters_count("Python 3.6.3"))
#[3, 9]

def numbers_letters_count(my_str):
    """Get a string. return a list where the first item represents the amount of numbers in the string 
    and the second item represents the amount of any charecter (including spaces etc) which is not a string.
    :param my_str: input string to check
    :type my_str: string
    :return: list with two items of results
    :rtype: list
    """
    collect_results = [ 0 ,0 ]
    for chr in my_str:
        #print(type(chr))
        if  chr.isnumeric() :
            collect_results[0] += 1
        else: collect_results[1] += 1
    return(collect_results)

input_string = (input("Enter a string: "))
print(len(input_string))
result_list = numbers_letters_count(input_string)
print("There are: ", result_list[0], "numbers in the string and ", result_list[1], "characters")


