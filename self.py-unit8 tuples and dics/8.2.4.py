

def note():
    """
    >>> list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated',
     'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled',
      'greatening', 'lasted', 'resmelts']
    >>> sort_anagrams(list_of_words)
    [['deltas', 'desalt', 'slated', 'salted', 'staled', 'lasted'], 
    ['retainers', 'ternaries'], 
    ['pants'], 
    ['generating', 'greatening'], 
    ['smelters', 'termless', 'resmelts']]
    """

def check_anagrams(string, possible_anagram):
    result = False
    print("checking:", string, possible_anagram)
    if sorted(string) == sorted(possible_anagram):
        print(string, "and", possible_anagram, "are anagrams!")
        result = True
    return result

def sort_anagrams(list_of_strings):
    """ get a list of strings return the strings sorted by anagrams into separate lists
    """
    print("started function with strings:", list_of_strings)
    final_list = []
    i = 0
    while i < (len(list_of_strings)): #problem is here!!! isn't checking till  the end of the list
        list_of_anagrams = []
        string_to_check = list_of_strings[i]
        if string_to_check not in list_of_anagrams:
            list_of_anagrams.append(string_to_check)
        print("######################\nstring in loop is", list_of_strings[i], "checking string:", string_to_check, "added it to list of anagrams:",  list_of_anagrams)
        j = 1   
        while j < (len(list_of_strings)):
            print("comparing:",string_to_check, list_of_strings[j])
            if len(string_to_check) == len(list_of_strings[j]) and string_to_check != list_of_strings[j]: #can be an anagram but not identical
                print(string_to_check, list_of_strings[j], "might be anagrams..checking!")
                if (check_anagrams(string_to_check, list_of_strings[j])) and (list_of_strings[j]) not in list_of_anagrams :
                    print("they are anagrams!")
                    list_of_anagrams.append(list_of_strings[j])
                    print("adding", list_of_strings[j], "to results:", list_of_anagrams, "\n list of strings:")
                    print(list_of_strings)   
            j += 1
        i += 1
        print("***********************\nfinished checking:",string_to_check, "added to list of results:" , list_of_anagrams)
        print("string list", list_of_strings )
        #once we are done with the check loop the base string should be removed from the strings list
        final_list.append(list_of_anagrams)
    print("end of function:", final_list)                
    return final_list                            


list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating',
 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
print("the sorted list:", sort_anagrams(list_of_words))