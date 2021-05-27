
#>>> sequence_del("ppyyyyythhhhhooonnnnn")
#'python'
#>>> sequence_del("SSSSsssshhhh")
#'Ssh'
#>>> sequence_del("Heeyyy   yyouuuu!!!")
#'Hey you!'

def sequence_del(my_str):
    """The function gets a string and deletes any consecutive duplicate characters.
    :param my_str: input string
    :type my_str: string
    :return: string with duplicate characters omitted 
    :rtype: string
    """
    collect_results = []
    print(len(my_str))
    for items in range(len(my_str)-1) : 
        #print(my_str[i], chrs)
        if my_str[items] != my_str[items+1] :
            collect_results.append(my_str[items])
            #print(my_str[items])
    if collect_results[-1] != my_str[-1] :
        collect_results.append(my_str[-1])
    str_results = ''.join(collect_results)
    return(str_results)


input_string = input("Enter a string: ")
result = sequence_del(input_string)
print(result)


