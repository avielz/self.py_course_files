#has debug comments in place with ***
import my_py_lib
#my_py_lib.func1()

def welcome_scr():
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
    this func will get a param num_of_tries
    and will return the matching hangman image from the dict values
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
    """gets list of the letters guessed so far
        asks for input of new letter to guess and passes it on to check function
    """
    letter_guessed = input("Guess a letter: ")
    letter_guessed = letter_guessed.lower()  
    try_update_letter_guessed(num_of_tries, old_letters_guessed, secret_word, letter_guessed)
                                                  
    return None

def in_old(letter_guessed, old_letters_guessed):
    """gets a param with the letter that was guessed
        gets list of old letters guessed so far
        checks if letter was already guessed before and returns true if was or false if new guess
    """
    print("checking in old guesses if was guessed already, got params:\nletter_guessed:",letter_guessed,
    "\n old_letters_guessed:", old_letters_guessed)
    result = False
    if letter_guessed in old_letters_guessed:
        result = True
    print("***passing result check:", result)
    return result

def in_letter(letter_guessed, secret_word):
    """gets string of the guessed letter and the string of the secret word.
        checks if the letter is in the secret word. returns true if yes or false
    """
    print("***checking if in letter func-> got params:\n letter_guessed:", letter_guessed,
    "\n secret_word:", secret_word)
    result = False
    if letter_guessed in secret_word:
        result = True
    print("***passing result check:", result)
    return result

def update_guessed_letters(letter_guessed, old_letters_guessed):
    """gets a param with the letter that was guessed after it went through validation functions
        gets list of old letters guessed so far
        adds the latest letter to the list
        returns the updated list
    """
    old_letters_guessed.append(letter_guessed)

    return old_letters_guessed

def try_update_letter_guessed(num_of_tries, old_letters_guessed, secret_word, letter_guessed):
    """The function receives a string with the guessed letter and a list of all the previous guessed letters.
    and a string with the secret word.
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
    print("starting to validate guess -> my params:\\num of tries:",num_of_tries,"\n old_letters_guessed:",old_letters_guessed,
    "\n secret_word:", secret_word, "\n letter_guessed:",letter_guessed,"\n MAX_TRIES:",MAX_TRIES)
    if  not check_valid_input(letter_guessed):
        print("X...input not a valid char")
        guess_letter(num_of_tries, old_letters_guessed, secret_word)
    elif in_old(letter_guessed, old_letters_guessed): 
        old_letters_string = "->".join(old_letters_guessed) # to display the already guessed letters
        print("X\n", old_letters_string)
        guess_letter(num_of_tries, old_letters_guessed, secret_word)
    elif in_letter(letter_guessed, secret_word):
        old_letters_guessed = update_guessed_letters(letter_guessed, old_letters_guessed)
        show_hidden_word(secret_word, old_letters_guessed)
        if check_win(num_of_tries, old_letters_guessed, secret_word):
            print("WIN")
        else: guess_letter(num_of_tries, old_letters_guessed, secret_word)
    else : #all other options have been checked so time to get on with the hanging!
        print(":(")
        old_letters_guessed = update_guessed_letters(letter_guessed, old_letters_guessed)
        print_hangman(num_of_tries+1)
        add_try(num_of_tries, old_letters_guessed, secret_word) #from here will continue on from add try
        
    return None

def check_valid_input(letter_guessed):
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
    print("check valid input func->", letter_guessed)
    if len(letter_guessed) > 1 or not letter_guessed.isalpha() :
        letter_test = False
    else : letter_test = True

    return letter_test

def show_hidden_word(secret_word, old_letters_guessed):
    """ get two params: secret_word string of the word the user needs to guess + old_letters_guessed
    a list with the guessed letters so far.
    the function returns a string with the letters guessed correctly in their palcement and underscore
    for the rest of the unguessed letters.

    *** problem seems like result list will erase every time so need to solve this- pass it from main
    also that before this function is called make sure that old letters guessed has been updated with latest
    letter guesses- because this function doesnt need and doesnt get letter update_guessed_letters
    and seems that it is not updated ***
    """
    print("***started show hidden word func-> got params:\n secret_word:", secret_word,
    "\n old_letters_guessed:",old_letters_guessed)      

    result_list = [None for x in range(len(secret_word))] #so no range problems for the loops and easy to verify
    for letter in old_letters_guessed :
        for i in range(len(secret_word)) :
            print("***old letter guessed: ", letter, "letter in word: ", secret_word[i])
            if letter == secret_word[i] :
                print(i, "*** out of:", len(secret_word))
                result_list[i] = secret_word[i]
                print("***", result_list)
            else: 
                if result_list[i] == None :
                    result_list[i] = "_"
                    print("***", result_list)

    result_string = " ".join(result_list)

    print(result_string)

    return None

def check_win(num_of_tries, old_letters_guessed, secret_word):
    """ get two params: string secret_word and a list of old_letters_guessed.
    check if all letters in secret word appear in list of guessed letters.
    if yes prints WIN and game finishes
    if no invokes add try function
    returns boolean
    """
    result = False
    result_sum = 0
    for letter in secret_word:
        if letter in old_letters_guessed :
            result_sum += 1
    if result_sum == len(secret_word):
        result = True
    #*** no need- add try is only for failed tries. 
    # else: add_try(num_of_tries, old_letters_guessed, secret_word)

    return result

def add_try(num_of_tries, old_letters_guessed, secret_word):
    """gets param with current number of tries. adds one try to number of tries and invokes function to test if 
    number of tries is under allowed number
    returns None
    """
    num_of_tries += 1
    try_under_max(num_of_tries, old_letters_guessed, secret_word)

    return None

def try_under_max(num_of_tries, old_letters_guessed, secret_word):
    """ gets two int params- current tries and allowed tries. checks if current is under allowed
        if not and max tries has been reached prints Lose and game finishes
        if under max tries invokes the function to continue guessing process
        returns none
    """
    if num_of_tries < MAX_TRIES:
        guess_letter(num_of_tries, old_letters_guessed, secret_word)
    else:
        print("LOSE")
    
    return None

def choose_word(file_path, index):
    """ get 2 params: file path, index - int that points to the place of a word in the file
    the function will return tuple:
    number of words in the file (excluding doubles)
    the word according to the index number which will be used as the secret word to guess
    -note make provision that index number start is 1 (not 0) - don't offset and miss first word in file
    -if index number > number of words in the file -> continue the count of words from begining of file
    """
    f = open(file_path, "r")
    word_data = f.read()
    f.close() 

    #print("this is the read data from the file before work:\n", word_data, type(word_data))
    word_list = word_data.split(" ")
    #print("this is the data after split \" \" method to turn string to list:\n", word_list,
    #type(word_list), "\n")

    #choose word with index number
    amount_words = len(word_list)
    #print("words in list with doubles:", amount_words, "\n")
    
    #check if index > than word count
    if index > amount_words:
        while amount_words < index:
            index = index - amount_words
        #print("index number more than amount of words, adjusted index number:", index, "\n")
    
    #choose word - according to result example they gave with index 15 chooses from list with duplicates!
    # no sweat if want to change. just bump up the duplicates sort and then run the index check
    # on the sorted list with no duplicates
    chosen_word = word_list[index-1]

    #for tuple number of words in file excluding duplicates
    wordlist_no_duplicates = list(dict.fromkeys(word_list))
    #print(wordlist_no_duplicates,"\n")
    wordlist_length = len(wordlist_no_duplicates)
    #print(wordlist_length)

    return chosen_word

def main():
  num_of_tries = 0
  old_letters_guessed = [""]

  welcome_scr()
  FIXED_PATH = r"C:\Users\avielz\Downloads\hangman\hangman_project\words.txt"
  print(FIXED_PATH)
  file_path = input("Enter file path (you can copy paste the above): ")
  index_input = int(input("Enter index: "))
  print_hangman(num_of_tries)

  secret_word = choose_word(file_path, index_input)
  print("***secret word chosen from file:", secret_word)
  show_hidden_word(secret_word, old_letters_guessed)

  #while try_under_max(num_of_tries, MAX_TRIES) and not check_win(secret_word, result_string):
  guess_letter(num_of_tries, old_letters_guessed, secret_word)
  
#global variables -so don't need to pass on
MAX_TRIES = 6

if __name__ == "__main__":
  main()



