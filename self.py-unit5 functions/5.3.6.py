
#>>> filter_teens()
#0
#>>> filter_teens(1, 2, 3)
#6
#>>> filter_teens(2, 13, 1)
#3
#>>> filter_teens(2, 1, 15)
#18
 
def filter_teens(a, b, c):
    print("started filter_teens fun, got a,b,c:", a, b, c)
    fixed_a = fix_age(a) 
    fixed_b = fix_age(b)
    fixed_c = fix_age(c)
    result = fixed_a + fixed_b + fixed_c
    return result

def fix_age(age = 13):
    print("start fix_age fun, got age:", age)
    if ((age >= 12) and (age <= 19)) and ((age != 15) and (age != 16)):
        fixed_age = 0
    else:
        fixed_age = age
    print(age, fixed_age)
    return fixed_age

a = int(input("enter 1st age: "))
b = int(input("enter 2nd age: "))
c = int(input("enter 3rd age: "))
result_to_print = filter_teens(a, b ,c)
print("The sum of ages", a, b, c, "is:", result_to_print)
