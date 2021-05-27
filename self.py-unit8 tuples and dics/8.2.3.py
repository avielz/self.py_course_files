

def note():
    """
    >>> first_tuple = (1, 2)
    >>> second_tuple = (4, 5)
    >>> mult_tuple(first_tuple, second_tuple)
    ((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))

    >>> first_tuple = (1, 2, 3)
    >>> second_tuple = (4, 5, 6)
    >>> mult_tuple(first_tuple, second_tuple)
    ((1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 1),
     (5, 1), (6, 1), (4, 2), (5, 2), (6, 2), (4, 3), (5, 3), (6, 3))
    """

def mult_tuple(tuple1, tuple2):
    """ get two tuples, return a tuple of all the pairs that can be combined from the passed arguments.
    tuple3 = None
    for i in range(len(tuple1)) :
        for j in range(len(tuple2)) :
            tuple3 = tuple3, (tuple1[i],tuple2[i]),(tuple2[i],tuple1[i],)
    """
    res =  [(b, a) for a in tuple1 for b in tuple2] + ["end"]
    res = res + [(b, a) for a in tuple1 for b in tuple2]
    #2 methods- second from course notes
    list = []
    for a in range(len(tuple1)):
        for b in range(len(tuple2)):
            list = list , (tuple1[a],tuple2[b]) , (tuple2[b],tuple1[a])
        
    print(tuple(res))
    print(list)

    return None

first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
mult_tuple(first_tuple, second_tuple)