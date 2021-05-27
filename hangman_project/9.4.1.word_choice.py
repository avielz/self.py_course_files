
def note():
    """
    דוגמה לקובץ טקסט שמכיל רשימת מילים, שנקרא words.txt
    hangman song most broadly is a song hangman work music work broadly is typically
    דוגמאות להרצה של הפונקציה choose_word עם הקובץ words.txt
    >>> choose_word(r"c:\words.txt", 3)
    (9, 'most')
    >>> choose_word(r"c:\words.txt", 15)
    (9, 'hangman')
    """

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

    result_tuple = (wordlist_length, chosen_word)

    return result_tuple

read_path = r"C:\Users\avielz\Downloads\hangman\hangman_project\words.txt"
input_num = int(input("Input number to choose word:"))
print(choose_word(read_path, input_num))

