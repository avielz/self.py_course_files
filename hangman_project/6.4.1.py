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

def check_valid_input(letter_guessed, old_letters_guessed):
    """The function receives a string with the guessed letter and a list of all the previous guessed letters.
    checks if the guessed letter is legitimate and if not retrun false value:
    letter has been guessed before
    not a legitimate character Cheking that the guessed letter is a valid letter.
   :param letter_guessed: the letter the user guessed already in lower case
   :param letter_test: holds the result of the validation test
   :type letter_guessed: string
   :type letter_test: boolean
   :return: The result of the letter test
   :rtype: boolean
    """
    letter_test = False
    if letter_guessed not in old_letters_guessed:
        if len(letter_guessed) > 1 and not letter_guessed.isalpha() :
            letter_test = False
        elif len(letter_guessed) > 1 :
            letter_test = False
        elif not letter_guessed.isalpha() :
            letter_test = False
        else : letter_test = True
    return(letter_test)

guessed_letter = input("Guess a letter: ")
letter_guessed_lower = guessed_letter.lower()

old_letters = ['a', 'b', 'c']
check_letter = check_valid_input(letter_guessed_lower, old_letters)
print(check_letter)


#Please enter a word: hangman
#_ _ _ _ _ _ _

#i thought the solution was based on the replace method but it turned out to be much more simple!
#new_string = input_string[0] + sliced_input_string.replace(first_chr, "e")

#guessed_word = input("Please enter a word: ")
#spaces = (len(guessed_word) * "_ ")
#print(spaces)