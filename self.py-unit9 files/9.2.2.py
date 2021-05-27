

def note():
    """
    >>> copy_file_content("copy.txt", "paste.txt")
    הקובץ paste.txt לאחר ההרצה לעיל של הפונקציה copy_file_content:

    Copy this text to another file.
    """

def copy_file_content(source, destination):
    """ get two strings of file paths
    function copies source content to destination
    source.txt Copy this text to another file.
    destination.txt  
    """
    the_source = open(source, "r")
    the_destination = open(destination, "r+")

    source_content = the_source.read()
    print("source content:", source_content, "\n")

    destination_content = the_destination.read()
    print("Destination current content:", destination_content, "\n")

    the_destination.write(source_content)
    print("copied content:", destination_content)

    the_source.close()
    the_destination.close()
    return None


source_path = r"C:\Users\avielz\Downloads\hangman\hangman-unit9 files\sampleFile.txt"
destination_path = r"C:\Users\avielz\Downloads\hangman\hangman-unit9 files\sunbathing.txt"

copy_file_content(source_path, destination_path)