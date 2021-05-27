
def welcome_scr():
    """called at the begining to print welcome screen. 
        gets none returns none
        :param HANGMAN_ASCII_ART: the open screen artwork
        :type HANGMAN_ASCII_ART: string
        :return: none
        :rtype: 
    """
    HANGMAN_ASCII_ART = ("""Welcome to the game Hangman\n _    _
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |
                    |___/""")

    print(HANGMAN_ASCII_ART)

    return None

def print_hangman(num_of_tries):
    """ create fixed global dict var named HANGMAN_PHOTOS.
    the dict will hold the 7 stages of images of the hanged man
    this func will get a param num_of_tries and print the relevant image.
    and will print the matching hangman image from the dict values
        :param num_of_tries: holds the number of tries (only failed counted)
        :param HANGMAN_PHOTOS: a dictionairy - key is integer number of tries, value is a string of the art
        :type num_of_tries: int
        :type HANGMAN_PHOTOS: dict
        :return: none
        :rtype:
    """
#dictionairy of the hangman images
    HANGMAN_PHOTOS = {
0 : """
x-------x
""",
1 : """
x-------x
    |
    |
    |
    |
    |
""",
2 : """
x-------x
    |   |
    |   0
    |
    |
    |
""",
3 : """
x-------x
    |   |
    |   0
    |   |
    |
    |
""",
4 : """
x-------x
    |   |
    |   0
    |  /|\\
    |
    |
""",
5 : """
x-------x
    |   |
    |   0
    |  /|\\
    |  /
    |
""",
6 : """
x-------x
    |   |
    |   0
    |  /|\\
    |  / \\
    |
"""
}

    hangman_image = HANGMAN_PHOTOS[num_of_tries]
    print(hangman_image)

    return None

def guess_letter(num_of_tries, old_letters_guessed, secret_word):
    """
    holds the guess cycle till outcome.
        asks for input of new letter to guess and converts it to lowercase.
        calls for next function to check if guess is valid
        if guess is valid checks if the letter is in the word and if yes will show the letter
        placement in the word and will also check if all letters were guessed and won
        if letter is not in the word will start hanging sequence.
            :param num_of_tries: holds the number of tries (only failed counted)
            :param old_letters_guessed: a list that collects letters that were guessed
            :param secret_word: holds the secret word that needs to be guessed
            :param letter_guessed: holds the charecter the user guessed
            :type num_of_tries: int
            :type old_letters_guessed: list
            :type secret_word: string
            :type letter_guessed: string
            :return: none
            :rtype:
    """
    letter_guessed = input("Guess a letter: ")
    letter_guessed = letter_guessed.lower()

    is_valid, old_letters_guessed = try_update_letter_guessed(old_letters_guessed, letter_guessed)
    #sending the guess to be validated and get boolean result + the updated guessed letters list

    if is_valid:
        if in_word(letter_guessed, secret_word):
            show_hidden_word(secret_word, old_letters_guessed)
            if check_win(old_letters_guessed, secret_word):
                print("WIN") #end of program
            else: guess_letter(num_of_tries, old_letters_guessed, secret_word)
        else : #hanging sequence: all other options have been checked so time to get on with the hanging!
            print(":(")
            print_hangman(num_of_tries+1)
            num_of_tries += 1
            if not try_under_max(num_of_tries):
                print("LOSE") #end of program
            else: guess_letter(num_of_tries, old_letters_guessed, secret_word)
    else: guess_letter(num_of_tries, old_letters_guessed, secret_word) #guess was not valid so starting over

    return None

def try_update_letter_guessed(old_letters_guessed, letter_guessed):
    """The function receives a string with the guessed letter and a list of all the previous guessed letters.
    checks if the guessed letter is legitimate- a valid character and not used before
    if valid - the function will add the letter to the guessed letters list and will return the list amd a true value
    if not valid the function will print the letter X and retrun false value.
    if letter was already used will print the letter X 
    and underneath a list of the guessed letters so far with -> between and retrun false value.
        :param old_letters_guessed: a list that collects letters that were guessed
        :param letter_guessed: holds the charecter the user guessed
        :type old_letters_guessed: list
        :type letter_guessed: string
        :return: result true or false if letter is valid and the updated list of letters guessed
        :rtype: boolean, list
    """
    result = True
    if  not check_valid_input(letter_guessed):
        print("X...input not a valid char")
        result = False
    elif in_old(letter_guessed, old_letters_guessed): 
        old_letters_string = "->".join(old_letters_guessed) # to display the already guessed letters
        print("X\n", old_letters_string)
        result = False
    else: old_letters_guessed = update_guessed_letters(letter_guessed, old_letters_guessed)
            
    return (result, old_letters_guessed)

def in_old(letter_guessed, old_letters_guessed):
    """gets a param with the letter that was guessed
        gets list of old letters guessed so far
        checks if letter was already guessed before and returns true if was or false if its a new guess
        :param old_letters_guessed: a list that collects letters that were guessed
        :param letter_guessed: holds the charecter the user guessed
        :type old_letters_guessed: list
        :type letter_guessed: string
        :return: the result if letter was already used
        :rtype:boolean
    """
    result = False
    if letter_guessed in old_letters_guessed:
        result = True
    
    return result

def in_word(letter_guessed, secret_word):
    """gets string of the guessed letter and the string of the secret word.
        checks if the letter is in the secret word. returns true if yes or false
        :param letter_guessed: holds the charecter the user guessed
        :param secret_word: holds the secret word
        :type letter_guessed: string
        :type secret_word: string
        :return: the result if letter is in secret word
        :rtype:boolean   
    """
    result = False
    if letter_guessed in secret_word:
        result = True

    return result

def update_guessed_letters(letter_guessed, old_letters_guessed):
    """gets a param with the letter that was guessed after it went through validation functions
        gets list of old letters guessed so far
        adds the latest letter to the list
        returns the updated list
        :param old_letters_guessed: a list that collects letters that were guessed
        :param letter_guessed: holds the charecter the user guessed
        :type old_letters_guessed: list
        :type letter_guessed: string
        :return: the updated list of letters guessed
        :rtype:list
    """
    old_letters_guessed.append(letter_guessed)

    return old_letters_guessed

def check_valid_input(letter_guessed):
    """The function receives a string with the guessed letter and a list of all the previous guessed letters.
    checks if the guessed letter is legitimate and if not retrun false value:
    letter has been guessed before
    not a legitimate character Cheking that the guessed letter is a valid letter.
   :param letter_guessed: the letter the user guessed already in lower case
   :type letter_guessed: string
   :return: The result of the letter test
   :rtype: boolean
    """
    if len(letter_guessed) > 1 or not letter_guessed.isalpha() :
        letter_test = False
    else : letter_test = True

    return letter_test

def show_hidden_word(secret_word, old_letters_guessed):
    """ get two params: secret_word string of the word the user needs to guess + old_letters_guessed
    a list with the guessed letters so far.
    the function returns a string with the letters guessed correctly in their palcement and underscore
    for the rest of the unguessed letters.
        :param old_letters_guessed: a list that collects letters that were guessed
        :param secret_word: holds the secret word
        :type old_letters_guessed: list
        :type secret_word: string
        :return: None
        :rtype:
    """  
    result_list = [None for x in range(len(secret_word))] #so no range problems for the loops and easy to verify
    for letter in old_letters_guessed :
        for i in range(len(secret_word)) :
            if letter == secret_word[i] :
                result_list[i] = secret_word[i]
            else: 
                if result_list[i] == None :
                    result_list[i] = "_"

    result_string = " ".join(result_list)

    print(result_string)

    return None

def check_win(old_letters_guessed, secret_word):
    """ get two params: string secret_word and a list of old_letters_guessed.
    check if all letters in secret word appear in list of guessed letters.
    if yes prints WIN and returns true
    if no returns false
    returns boolean
        :param old_letters_guessed: a list that collects letters that were guessed
        :param secret_word: holds the secret word
        :type old_letters_guessed: list
        :type secret_word: string
        :return: result of check if all letters in secret word were guessed
        :rtype: boolean
    """
    result = False
    result_sum = 0
    for letter in secret_word:
        if letter in old_letters_guessed :
            result_sum += 1
    if result_sum == len(secret_word):
        result = True

    return result

def try_under_max(num_of_tries):
    """ gets current tries and compares to global variable of max tries allowed.
        returns true in under or false if not.
            :param num_of_tries: integer keeping track of number of (failed!) tries.
            :type num_of_tries: int
            :return: result if tries are under set tries allowed 
            :rtype: boolean
    """
    result = False
    if num_of_tries < MAX_TRIES:
        result = True
            
    return result

def choose_word(file_path, index):
    """ get 2 params: file path, index - a number that points to the place of a word in the file.
    the function returns a word according to the index number which will be used as the secret word to guess.
    -note make provision that index number start is 1 (not 0) - don't offset and miss first word in file
    -if index number > number of words in the file -> continue the count of words from begining of file.
            :param file_path: the path to the file that holds the words.
            :parma: index: the number the user inputted to use as an index to choose the word.
            :type file_path: string
            :type index: int
            :return: the chosen word from the file of words
            :rtype: string
    """
    # get the data from the word file into a variable
    f = open(file_path, "r")
    word_data = f.read()
    f.close() 

    #de serialize the data into a list
    word_list = word_data.split(" ")

    #check if index > than word count adjust the index number 
    amount_words = len(word_list)
    if index > amount_words:
        while amount_words < index:
            index = index - amount_words
    
    #choose word from the list
    chosen_word = word_list[index-1]

    #according to result example in the assignment an index number of 15 chooses from list with duplicates!
    # if you want to choose from a list without duplicate words just bump up the following duplicates sort
    # line and then run the index check on wordlist_no_duplicates 
    # and assign the chosen-word from wordlist_no_duplicates [index-1]
    #wordlist_no_duplicates = list(dict.fromkeys(word_list))

    return chosen_word

def main():
# variables   
  num_of_tries = 0
  old_letters_guessed = [""]

  welcome_scr() #print the welcome screen

#get required input from user.
  file_path = input("Enter file path to words file: ")
  index_input = int(input("Enter index: "))

  print("\nLet's start!")
  print_hangman(num_of_tries) #print first stage of hangman art

  secret_word = choose_word(file_path, index_input) #get the secret word according to the index from the words file
  show_hidden_word(secret_word, old_letters_guessed) #print underlines according to the length of the chosen word

  guess_letter(num_of_tries, old_letters_guessed, secret_word) #start the process of the guessing till the outcome
  
#global variable -so don't need to pass on through functions
MAX_TRIES = 6

if __name__ == "__main__":
  main()



