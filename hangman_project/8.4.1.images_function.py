

def note():
    """
    >>> num_of_tries = 6
    >>> print_hangman(num_of_tries)
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |
    """

def print_hangman(num_of_tries):
    """ create fixed global dict var named HANGMAN_PHOTOS.
    the dict will hold the 7 stages of images of the hanged man
    this func will get a param num_of_tries
    and will return the matching hangman image from the dict values
    """
    hangman_image = HANGMAN_PHOTOS[num_of_tries]

    return hangman_image

HANGMAN_PHOTOS = {
1 : """
x-------x
""",
2 : """
x-------x
    |
    |
    |
    |
    |
""",
3 : """
x-------x
    |   |
    |   0
    |
    |
    |
""",
4 : """
x-------x
    |   |
    |   0
    |   |
    |
    |
""",
5 : """
x-------x
    |   |
    |   0
    |  /|\\
    |
    |
""",
6 : """
x-------x
    |   |
    |   0
    |  /|\\
    |  /
    |
""",
7 : """
x-------x
    |   |
    |   0
    |  /|\\
    |  / \\
    |
"""
}

num_of_tries = int(input("enter number of tries 1-7:"))
print("This is image", num_of_tries, ":\n\n", print_hangman(num_of_tries))