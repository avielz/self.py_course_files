

def note():
    """
    קובץ שנקרא findMe.txt:
    8,1,9,7,4,6,3,2
    הרצת הפונקציה who_is_missing על הקובץ findMe.txt:
    >>> who_is_missing("c:\findMe.txt")
    5
    לאחר ההרצה לעיל של הפונקציה who_is_missing נוצר קובץ חדש שנקרא found.txt:
    5
    """

def who_is_missing(file_name):
    """ get string of file paths
    the file has a list of int numbers 1 to n seperated by commas and jumbled
    one number in the flow is missing
    the func finds and returns the missing number
    creates a new file with the missing number
    """
    the_source = open(file_name, "r")
    temp_content = the_source.read()
    content_string_list = temp_content.split(",")
    #print(content_string_list)
    content_int_list = list(map(int, content_string_list))

    content_int_list.sort()
    print(content_int_list)
    i = 0
    x = 1
    missing_number = None
    while i < len(content_int_list):
        if x not in content_int_list:
            print("the missing number is:", x, "\n")
            missing_number = str(x) #have to pass a type of string to write into a file
            break
        i += 1
        x += 1
    
    if missing_number != None:
        create_file(missing_number)
    
    the_source.close()
    return None    

def create_file(number):
    new_file = open(r"C:\Users\avielz\Downloads\hangman\hangman-unit9 files\foundNumber.txt", "w")
    new_file.write(number)
    print("created a file for the missing number.")

    new_file.close()
    return None

path = r"C:\Users\avielz\Downloads\hangman\hangman-unit9 files\findMe.txt"
who_is_missing(path)