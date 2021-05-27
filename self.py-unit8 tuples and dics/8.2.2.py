
def note():
    """
    >>> products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    >>> sort_prices(products)
    [('bread', '9.0'), ('milk', '5.5'), ('candy', '2.5')]
    """

def second_item_tuple(tuple):
    """help function will get one tuple each time from sort key command in sort_prices function
    to return the second value of each index in the list
    """
    result = tuple[0][1]
    return result

def sort_prices(list_of_tuples):
    """ get a list of tuples that consist of an item and a price
    return a list of items sorted by price from high to low.
    """
    print(sorted(list_of_tuples, key=second_item_tuple, reverse=True))
    
    #n = 1 # N. . .
    #print(sorted(list_of_tuples, key=([x[1] for x in list_of_tuples])))
    #print(sorted(list_of_tuples, key=max[:][1]))
            
    return None


products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
sort_prices(products)