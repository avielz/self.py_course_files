

def note():
    """
    >>> my_mp4_playlist(r"c:\my_files\songs.txt", "Python Love Story")
    Tudo Bom;Static and Ben El Tavori;5:13;
    I Gotta Feeling;The Black Eyed Peas;4:05;
    Python Love Story;Unknown;4:15;
    Paradise;Coldplay;4:23;
    Where is the love?;The Black Eyed Peas;4:13;
    תוכן הקובץ songs.txt לאחר ריצת הפונקציה my_mp4_playlist

    Tudo Bom;Static and Ben El Tavori;5:13;
    I Gotta Feeling;The Black Eyed Peas;4:05;
    Python Love Story;Unknown;4:15;
    Paradise;Coldplay;4:23;
    Where is the love?;The Black Eyed Peas;4:13;

    songs.txt:
    Tudo Bom;Static and Ben El Tavori;5:13;
    I Gotta Feeling;The Black Eyed Peas;4:05;
    Instrumental;Unknown;4:15;
    Paradise;Coldplay;4:23;
    Where is the love?;The Black Eyed Peas;4:13;
    """

def my_mp4_playlist(file_path, new_song, write_path):
    """ get string of file path
    the file has a data of a playlist - see content above
    func write to new file: a param (new_song) with a string of the song name and replaces the song name on the third line in the file
    add a operation to check if there are less than 3 lines in the file to add empty lines so the song name is written in line 3.
    the func prints the content of the new file after its created.
    """

    #de-serialization

    f = open(file_path, "r")
    playlist_data = f.read()
    print("this is the read data from the file before work:\n", playlist_data, type(playlist_data))
    playlist_splitted_lines = playlist_data.split("\n")
    print("this is the data after split\\n method to turn string to list:\n", playlist_splitted_lines,
     type(playlist_splitted_lines), "\n")
    playlist_items = []
    for element in playlist_splitted_lines:
        playlist_items.append(element.split(";"))
    print("this is the data appended to final new list after ; split:\n", playlist_items,"\n")
    f.close() 

    #here add line length check operation 
    line_length = len(playlist_items)
    print("\nline length:" , line_length, "\n")
    if line_length < 3:
        while line_length < 3:
            playlist_items.append(["","","",""])
            line_length += 1
    appended_line_length = len(playlist_items)
    print("\nappended line length:" , appended_line_length, "\n")

    #replace new song name
    playlist_items[2][0] = new_song
    print("after adding new song:\n", playlist_items,"\n")
    
    #serialization
    input_file = open(write_path, "w")
    #join separate lists and return ";" between values
    rejoint_playlist_items = []
    for element in playlist_items:
        rejoint_playlist_items.append(";".join(element))
    print("after join ; try:\n", rejoint_playlist_items, "\n")

    #convert list back to string
    str1 = '\n'.join(rejoint_playlist_items)
    print("after turn back to string try with adding line down \\n:\n", str1, "\n")  

    #write string to new file
    input_file.write(str1)

    input_file.close()

    #read and print from new file
    file = open(write_path, "r")
    new_playlist_data = file.read()
    print("This is the list from the new file:\n", new_playlist_data)
     
    return None

# r"C:\Users\avielz\Downloads\hangman\hangman-unit9 files\songs.txt"
# can also run with this alternative text file path that has less than 3 lines to check condition:
# r"C:\Users\avielz\Downloads\hangman\hangman-unit9 files\songsLessLines.txt"

read_path = r"C:\Users\avielz\Downloads\hangman\hangman-unit9 files\songs.txt"
input_path = r"C:\Users\avielz\Downloads\hangman\hangman-unit9 files\new_songs.txt"
my_mp4_playlist(read_path, "Python Love Story",input_path )

