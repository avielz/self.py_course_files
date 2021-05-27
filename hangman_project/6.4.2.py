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
    else : 
        formated_string = "->".join(old_letters_guessed)
        print("X\n", formated_string)
    return(letter_test)

guessed_letter = input("Guess a letter: ")
letter_guessed_lower = guessed_letter.lower()

old_letters = ['a', 'p', 'c', 'f']
check_letter = try_update_letter_guessed(letter_guessed_lower, old_letters)
print(check_letter)


#Please enter a word: hangman
#_ _ _ _ _ _ _

#i thought the solution was based on the replace method but it turned out to be much more simple!
#new_string = input_string[0] + sliced_input_string.replace(first_chr, "e")

#guessed_word = input("Please enter a word: ")
#spaces = (len(guessed_word) * "_ ")
#print(spaces)