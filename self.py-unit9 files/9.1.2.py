

def note():
    """
    sampleFile.txt:
    i believe i can fly i believe i can touch the sky
    i think about it every night and day spread my wings and fly away

    >>> Enter a file path: c:\sampleFile.txt
    >>> Enter a task: sort
    ['about', 'and', 'away', 'believe', 'can', 'day', 'every', 'fly', 'i', 'it', 'my',
     'night', 'sky', 'spread', 'the', 'think', 'touch', 'wings']

    >>> Enter a file path: c:\sampleFile.txt
    >>> Enter a task: rev
    yks eht hcuot nac i eveileb i ylf nac i eveileb i
    yawa ylf dna sgniw ym daerps yad dna thgin yreve ti tuoba kniht i

    >>> Enter a file path: c:\sampleFile.txt
    >>> Enter a task: last
    >>> Enter a number: 1
    i think about it every night and day spread my wings and fly away
    """

def menu():
    """ get string with file path- file txt content to create is given above (text has single spaces)
    get action: last rev or sort
    sort- print all words (no spaces) as a sorted list with no doubles
    rev- print all chars in each line in reverse order
    last- get another int parameter (n) and print the last n lines in the file
    """
    path = r"C:\Users\avielz\Downloads\hangman\hangman-unit9 files\sampleFile.txt"

    #open file for reading
    input_file_1 = open(path, "r")

    #get user choice and invoke appropriate function
    print("\n")
    user_input = input("input action to perform on file: last rev sort or exit: ")
    print("\n")
    fields = {"the_" : user_input} #made a dic item (can maybe work in other data types) of the function name
    #found solution on stackoverflow on how to single out a string value and use it as a function name
    import sys
    getattr(sys.modules[__name__], "%s" % fields["the_"])(input_file_1) #invokes the desired function
      
    input_file_1.close()
    return None

def sort(file):
    """sort- print all words (no spaces) as a sorted list with no doubles"""
    file_string = file.read()
    file_list = []
    result_list =[]
    file_list = file_string.split(" ")
    #print(file_list)
    for words in file_list:
        #print(words)
        if words not in result_list:
            result_list.append(words)
            #print(result_list)

    result_list.sort() #does not work if try to print list with sort func- output: None
    print(result_list)
    menu()
    return None

def rev(file):
    """rev- print all chars in each line in reverse order"""
    lines = file.readlines() #list of lines
    for line in lines:
        print(line[::-1])

    menu()
    return None

def last(file):
    """last- get another int parameter (n) and print the last n lines in the file"""
    lines = file.readlines() #list of lines
    x = len(lines)
    input_string = "how many lines out of total", x, "lines from the bottom would you like to print?:"
    how_many = int(input(input_string))
    print(' '.join(lines[x - how_many:]))
    
    menu()
    return None

def exit(file):
    print("It was fun, Bye!")
    return None

menu()

