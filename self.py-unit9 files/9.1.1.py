

#>>> are_files_equal("c:\vacation.txt", "c:\work.txt")
#False

def are_files_equal(file1, file2):
    """ func gets two params of file path (string)
    checks if files are identical
    return true or false
    """
    input_file_1 = open(file1, "r")
    input_file_2 = open(file2, "r")

    file1 = input_file_1.read()
    file2 = input_file_2.read()
    print(type(file1), file1, type(file2), file2)

    result =False
    if file1 == file1:
        result = True

    input_file_1.close()
    input_file_2.close()
    return result



first_file = r"C:\Users\avielz\Downloads\hangman\hangman-unit9 files\vacation.txt"
second_file = r"C:\Users\avielz\Downloads\hangman\hangman-unit9 files\sunbathing.txt"
result = are_files_equal(first_file, second_file)

#from pathlib import Path
#Path(r'c:\temp\foo.bar')
#result = are_files_equal(Path(r"c:\vacation.txt"), Path(r"c:\work.txt"))
print("are the files identical?:", result)


