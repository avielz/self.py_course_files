
#>>> print(seven_boom(17))
#['BOOM', 1, 2, 3, 4, 5, 6, 'BOOM', 8, 9, 10, 11, 12, 13, 'BOOM', 15, 16, 'BOOM']

def seven_boom(end_number):
    """The function gets a positive int. returns a list of numbers from 0 till the given number (including), but certain values are replaced with the string 'BOOM' if meet the conditions:
    the value is a multiple of 7
    the value has the digit 7
    :param end_number: range end
    :type end_number: int
    :return: list with number in the range and values that meet criteria changed to 'BOOM'
    :rtype: list
    """
    collect_results = []
    for number in range((end_number)) : 
        #print(type(chr))
        number += 1
        if number % 7 == 0 or number // 10 == 7 or number % 10 ==7 :
            collect_results.append("BOOM")
        else: collect_results.append(number)
    return(collect_results)

end_range = int((input("Enter top value for the range: ")))
result_list = seven_boom(end_range)
print(result_list)


