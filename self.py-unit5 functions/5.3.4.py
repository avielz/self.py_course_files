
#>>> last_early("happy birthday")
#True
#>>> last_early("best of luck")
#False
#>>> last_early("Wow")
#True
#>>> last_early("X")
#False


input_str = input("Enter a string and I will check if the last chr appears before: ")
input_str= input_str.lower()

def last_early(my_str):
    if my_str[-1] in my_str[:-2]:
        result = True
        print(result)
    else: result = False
    return result


result_to_print = last_early(input_str)
print("The chr ",input_str[-1], "appears before the end: ",  result_to_print)
