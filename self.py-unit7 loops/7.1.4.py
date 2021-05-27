
#>>> squared_numbers(4, 8)
#[16, 25, 36, 49, 64]
#>>> squared_numbers(-3, 3)
#[9, 4, 1, 0, 1, 4, 9]

def squared_numbers(start, stop):
    """ get to int numbers stop, start (start<=stop)
    return a list with all the squared numbers between start and stop.
   :param start: start number for loop
   :param stop: end number for loop
   :type start: int
   :type stop: int #needs to be smaller than start
   :return: list of squared values between start and stop including
   :rtype: list
    """
    collect_results = []
    while start <= stop :
        collect_results.append(start**2)
        start += 1
    return(collect_results)

start = int(input("Enter start number: "))
stop = int(input("Enter end number (larger than start): "))
squared_list = squared_numbers(start, stop)
print("The squared numbers between", start, "and", stop, ":", squared_list)


