
def note():
    """
    print(arrow('*', 5))
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
    """

def arrow(my_char, max_length):
    """function gets two params: a char and max length
    the function will return a string with a shape of an 'arrow'
    built from the given char and the given centers length.
    """
    arrow_string1 = ""
    arrow_string2 = ""
    start_length = 1
    while start_length <= max_length :
        arrow_string1 = arrow_string1 + (my_char +" ") * start_length + "\n"
        start_length += 1
    while max_length > 0 :
        arrow_string2 = arrow_string2 + (my_char +" ") * (max_length - 1) + "\n"
        max_length += -1
    arrow_string = arrow_string1 + arrow_string2
    return arrow_string

char = input("Enter a charecter to use: ")
length = int(input("Enter the length of the arrow center: "))

result = arrow(char, length)
print(result)






