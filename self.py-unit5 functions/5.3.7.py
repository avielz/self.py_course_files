
#>>> chocolate_maker(3, 1, 8)
#True
#>>> chocolate_maker(3, 1, 9)
#False
#>>> chocolate_maker(3, 2, 10)
#True
 
BIG_LENGTH = 5
SMALL_LENGTH = 1

def chocolate_maker(small, big, x):
    big_amount = big
    small_amount = x % BIG_LENGTH
    if x <= small * SMALL_LENGTH + big * BIG_LENGTH and small >= small_amount:
        big_amount = x // BIG_LENGTH
        if big_amount > big:
            big_amount = big
            small_amount = x % big
        result = True
    else: result = False
    return (result, small_amount, big_amount)

def print_result(result):
    if result[0]:
        print("A chocolate bar of", x, "cm, made of", a, "small pieces and", b, "big ones- is possible using",result[1], "small pieces and", result[2], "big ones")
    else: print("it's not possible to make such a chocolate bar with those pieces")

a = int(input("enter amount of small pieces: "))
b = int(input("enter amount og big pieces: "))
x = int(input("enter required length: "))

result_to_print = chocolate_maker(a, b ,x)
print_result(result_to_print)

