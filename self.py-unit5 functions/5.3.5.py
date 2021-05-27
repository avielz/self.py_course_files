
#>>> distance(1, 2, 10)
#True
#>>> distance(4, 5, 3)
#False

#abs(num)


#user_input = input("Enter 3 numbers, I will check if they are close: ")
#int_user_input = [int(x) for x in user_input]
#a, b, c = user_input.split()
#input_str = input("Enter 3 numbers, I will check if they are close: ")


def distance(num1, num2, num3):
    if ((abs(num2 - num1) == 1) or (abs(num3 - num1) == 1)) and ((abs(num2-num1)>=2) or (abs(num3-num1)>=2)):
        result = True
        print(result)
    else: result = False
    return result

a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
c = int(input("enter 3rd number: "))
result_to_print = distance (a, b ,c)
print("The numbers", a, b, c, "meet the condition:", result_to_print)
