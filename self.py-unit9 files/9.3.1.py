

def note():
    """
    >>> print(my_mp3_playlist(r"c:\my_files\songs.txt"))
    ("Tudo Bom", 5, "The black Eyed Peas")

    songs.txt:
    Tudo Bom;Static and Ben El Tavori;5:13;
    I Gotta Feeling;The Black Eyed Peas;4:05;
    Instrumental;Unknown;4:15;
    Paradise;Coldplay;4:23;
    Where is the love?;The Black Eyed Peas;4:13;
    """

def my_mp3_playlist(file_path):
    """ get string of file path
    the file has a data of a playlist - see content above
    func returns the following tuple:
    string with name of longest song
    int of number of songs in playlist
    string of singer who appears most
    """
    the_source = open(file_path, "r")
    temp_content = the_source.read()
    #print(temp_content, "\n")
    content_string_list = temp_content.split("\n")
    #print(content_string_list, "\n")
    playlist_items = [] #create new list with separated items
    for element in content_string_list:
        playlist_items.append(element.split(";"))
    #print(playlist_items)
    for lists in playlist_items:
        #get rid of created last empty space item on lists 
        del lists[-1]
    #print(playlist_items)

    #print(longest_song(playlist_items))
    #print(num_songs_in_list(playlist_items))
    #print(singer_most(playlist_items))

    thistuple = tuple((longest_song(playlist_items), num_songs_in_list(playlist_items), singer_most(playlist_items)))

    the_source.close()
    return thistuple

def singer_most(playlist_items):
    from collections import Counter
    #using a library method
    counter = Counter(playlist_items[0])
    #print("counter:", counter)
    for i in playlist_items[1:]: 
        counter.update(i)

    result = counter.most_common()
    
    #print("most commom singer:", result[0][0])
    return result[0][0] #the most appearing value is placed in the first index of the list

def num_songs_in_list(playlist_items):
    """return int of number of songs in playlist
    """
    result = len(playlist_items)
    #print("number of songs:", result)
    return result

def longest_song(playlist):
    """ get the playlist
    separate the time length element to minutes and seconds
    convert minutes and seconds to int
    find biggest time value
    return song name with biggest time value
    """
    i = 0
    temp_time_song_list = []
    while i < len(playlist):
        #get list of times string
        temp_time_song_list.append(playlist[i][2])
        i += 1
    #print(temp_time_song_list,"\n")

    #better method to deal with time length
    time_in_seconds = []
    for time in temp_time_song_list:
        #sending each time string to help func to convert to int seconds and create a list
        time_in_seconds.append(get_sec(time))

    #find the index of longest song in the new list
    max_value_seconds = max(time_in_seconds) #Return the max value of the list.
    max_index = time_in_seconds.index(max_value_seconds)

    import datetime
    #if i want to see the value in h:mm:ss format again. although can always just point to original value in list
    max_value_time_string = str(datetime.timedelta(seconds=max_value_seconds)) 

    #print("""\n\n************************\n
    #longest song time:
    #index number:
    #song name:
    #**************************************\n
    #""", max_value_time_string, max_index, playlist[max_index][0])
    
    return playlist[max_index][0]

def get_sec(time_str):
    """Get Seconds from time."""
    m, s = time_str.split(':')
    return int(m) * 60 + int(s) 

#this was the original script i used to deal with the time string- took me hours
    playlist_items_split_time = []
    for time in temp_time_song_list:
        #split time strings to minute and seconds string
        playlist_items_split_time.append(time.split(":"))
    print(playlist_items_split_time, "\n")
    j = 0
    while j < len(playlist_items_split_time):
        k = 0
        while k < 2:
        #convert minutes Seconds to int.
            playlist_items_split_time[j][k] = int(playlist_items_split_time[j][k])
            k += 1
        j += 1
    print(playlist_items_split_time)

    #find index with largest minutes
    j = 0
    temp_minutes_list = []
    while j < len(playlist_items_split_time):
        temp_minutes_list.append(playlist_items_split_time[j][0])
     
        j += 1
    print(temp_minutes_list,"\n") 

    #find largest minutes value and its list index -if there is a tie send to compare seconds
    largest = 0
    largest_index = -1
    largest_minute_index_list = []
    i = 0
    for minutes in temp_minutes_list:
        if minutes > largest:
            largest = minutes
            largest_index = i
        elif minutes == largest:
            largest_minute_index_list.append(i)
    #if there are songs with same minutes length- invoke compare seconds sequence
    if len(largest_minute_index_list) > 1:
        longest_time = compare_seconds(largest_minute_index_list, playlist_items_split_time)
        longest_song = playlist[longest_time][0]
    else: 
        print("index of longest song", largest_index)    
        longest_song = playlist[largest_index][0]

    
    #largest_minute_index_list = [0 , 3]
    #longest_time2 = compare_seconds(largest_minute_index_list, playlist_items_split_time)
    #longest_song2 = playlist[longest_time2][0]

    return longest_song#, longest_song2

#def compare_seconds(minutes_index_values, list_times):
    print(minutes_index_values, list_times)
    temp_list = []
    #get the seconds from the equal biggest minutes
    for items in minutes_index_values:
        temp_list.append(list_times[items][1])
    print("seconds list", temp_list)
    #find largest seconds and its index value
    largest = 0
    for seconds in temp_list:
        if seconds > largest:
            largest = seconds
    print("largest seconds is:", largest)
    
    #find index of largest seconds in list
    largest_index = 0
    i = 0
    for items in list_times:
        print("items in the loop:", items, "comparing", largest, "to", items[1:])
        if items[1:] == [largest]:
            largest_index = i
        print("i:", i)
        i +=1

    print("index of largest seconds is:", largest_index)
    return largest_index 

path = r"C:\Users\avielz\Downloads\hangman\hangman-unit9 files\songs.txt"
print(my_mp3_playlist(path))
