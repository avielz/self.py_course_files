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

#Guess a letter: ab
#E1
#Guess a letter: $
#E2
#Guess a letter: app$
#E3

guessed_letter = input("Guess a letter: ")
guessed_letter_lower = guessed_letter.lower()
if len(guessed_letter_lower) > 1 and not guessed_letter_lower.isalpha() :
    letter_output = "E3"
elif len(guessed_letter_lower) > 1 :
    letter_output = "E1"
elif not guessed_letter_lower.isalpha() :
    letter_output = "E2"
else : letter_output = guessed_letter_lower

print(letter_output)

#Please enter a word: hangman
#_ _ _ _ _ _ _

#i thought the solution was based on the replace method but it turned out to be much more simple!
#new_string = input_string[0] + sliced_input_string.replace(first_chr, "e")

#guessed_word = input("Please enter a word: ")
#spaces = (len(guessed_word) * "_ ")
#print(spaces)