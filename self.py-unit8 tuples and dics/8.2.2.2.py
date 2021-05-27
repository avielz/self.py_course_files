
def note():
    """
    >>> products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    >>> sort_prices(products)
    [('bread', '9.0'), ('milk', '5.5'), ('candy', '2.5')]
    """


def sort_prices(list_of_tuples):
    """ get a list of tuples that consist of an item and a price
    return a list of items sorted by price from high to low.
    """
    sorted_list = sorted(((price, item) for item, price in list_of_tuples), reverse=True)      
    return sorted_list


products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(sort_prices(products))