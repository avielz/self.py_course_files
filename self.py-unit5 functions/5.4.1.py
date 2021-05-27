


def func(num1, num2):
    """Divide two numbers.
   :param num1: first number value
   :param num2: second number value
   :type num1: int
   :type num2: int
   :return: The result of deviding num1 by num2
   :rtype: int
   """
    return int(num1/num2)

def main():
    # Call the function func
    x = int(input("Enter 1st number:"))
    y = int(input("Enter 2nd number:"))
    result = func(x, y)
    print(x,"/",y,"=",result)

if __name__ == "__main__":
    main()

help(func)
#func.__doc__  didnt work


