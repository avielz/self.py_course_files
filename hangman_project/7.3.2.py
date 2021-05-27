#hangman code learning python

HANGMAN_ASCII_ART = ("""Welcome to the game Hangman\n _    _
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \'
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |
                    |___/""")


print(HANGMAN_ASCII_ART)


#import random
#print (random.randint(5,10))

MAX_TRIES = 6
print(MAX_TRIES)

#>>> is_valid_input('a')
#True
#>>> is_valid_input('A')
#True
#>>> is_valid_input('$')
#False
#>>> is_valid_input("ab")
#False
#>>> is_valid_input("app$")
#False
#Guess a letter: ab
#E1
#Guess a letter: $
#E2
#Guess a letter: app$
#E3
#>>> old_letters = ['a', 'b', 'c']
#>>> check_valid_input('C', old_letters)
#False
#>>> check_valid_input('ep', old_letters)
#False
#>>> check_valid_input('$', old_letters)
#False
#>>> check_valid_input('s', old_letters)
#True
#>>> old_letters = ['a', 'p', 'c', 'f']
#>>> try_update_letter_guessed('A', old_letters)

#7.3.2

def note():
    """ >>> secret_word = "friends"
    >>> old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    >>> print(check_win(secret_word, old_letters_guessed))
    False

    >>> secret_word = "yes"
    >>> old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    >>> print(check_win(secret_word, old_letters_guessed))
    True
    """

def check_win(secret_word, old_letters_guessed):
    """ get two params: string secret_word and a list of old_letters_guessed.
    check if all letters in secret word appear in list of guessed letters.

    """
    result_sum = 0
    for letter in secret_word:
        if letter in old_letters_guessed :
            result_sum += 1
    if result_sum == len(secret_word):
        result = True
    else: result = False
    print(result_sum, len(secret_word))
    return result

def note():
    """
    >>> secret_word = "mammals"
    >>> old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    >>> print(show_hidden_word(secret_word, old_letters_guessed))
    m _ m m _ _ s
    """

def show_hidden_word(secret_word, old_letters_guessed):
    """ get two params: secret_word string of the word the user needs to guess + old_letters_guessed
    a list with the guessed letters so far.
    the function returns a string with the letters guessed correctly in their palcement and underscore
    for the rest of the unguessed letters.
    """
    
    result_list = [None for x in range(len(secret_word))] #so no range problems for the loops and easy to verify
    for letter in old_letters_guessed :
        for i in range(len(secret_word)) :
            #print("old letter guessed: ", letter, "letter in word: ", secret_word[i])
            if letter == secret_word[i] :
                #print(i, "out of:", len(secret_word))
                result_list[i] = secret_word[i]
                #print(result_list)
            else: 
                if result_list[i] == None :
                    result_list[i] = "_"
                    #print(result_list)
    result_string = " ".join(result_list)
    return(result_string)

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """The function receives a string with the guessed letter and a list of all the previous guessed letters.
    checks if the guessed letter is legitimate- 
    if yes - the function will add the letter to the guessed letters list and will return a true value
    if not valid the function will print the letter X and underneath a list of the guessed letter with -> between and retrun false value.
    a letter guessed is not valid if:
    letter has been guessed before
    not a legitimate character.
   :param letter_guessed: the letter the user guessed already in lower case
   :param letter_test: holds the result of the validation test
   :type letter_guessed: string
   :type letter_test: boolean
   :return: The result of the letter test
   :rtype: boolean
    """
    print("started guessed letter function")
    letter_test = False
    if letter_guessed not in old_letters_guessed:
        if len(letter_guessed) > 1 and not letter_guessed.isalpha() :
            letter_test = False
        elif len(letter_guessed) > 1 :
            letter_test = False
        elif not letter_guessed.isalpha() :
            letter_test = False
        else : 
            letter_test = True
    if letter_test == True: 
        old_letters_guessed.append(letter_guessed)
        print("good job. added the letter: ", letter_guessed_lower, old_letters_guessed)
    else : 
        formated_string = "->".join(old_letters_guessed)
        print("X\n", formated_string)
    return(letter_test, old_letters_guessed)

secret_word = "yes"
old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']

guessed_letter = input("Guess a letter: ")
letter_guessed_lower = guessed_letter.lower()

check_letter = try_update_letter_guessed(letter_guessed_lower, old_letters_guessed)

#print(show_hidden_word(secret_word, old_letters_guessed))

print(check_win(secret_word, old_letters_guessed))

#Please enter a word: hangman
#_ _ _ _ _ _ _

#i thought the solution was based on the replace method but it turned out to be much more simple!
#new_string = input_string[0] + sliced_input_string.replace(first_chr, "e")

#guessed_word = input("Please enter a word: ")
#spaces = (len(guessed_word) * "_ ")
#print(spaces)