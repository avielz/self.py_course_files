
def menu():
    """get input number and call the coressponding func"""
    user_input = input("choose a number from 1-7 (8 to exit):") 
    #dynamic function invoking with no need to check the choice and do if scenario
    fields = {"the_" : "seq" + user_input} #made a dic item (can maybe work in other data types) of the function name
    #found solution on stackoverflow on how to single out a string value and use it as a function name
    import sys
    getattr(sys.modules[__name__], "%s" % fields["the_"])() #invokes the desired function

    return None

def seq1():
    """ get chioce print key of last name"""
    print("her last name is:", Mariah_Carey["last_name"])
    menu()
    return None

def seq2():
    """ get  print the month of her BD"""
    print("she was born in month:", Mariah_Carey["birth_date"][3:5])
    menu()
    return None

def seq3():
    """ get  print how many hobbies she has"""
    print("She has", len(Mariah_Carey["hobbies"]), "hobbies")
    menu()
    return None

def seq4():
    """ get  print her last hobby"""
    print("her last hobby is:", (Mariah_Carey["hobbies"][-1]))
    menu()
    return None

def seq5():
    """ get add cooking to her hobbies"""
    Mariah_Carey["hobbies"].append("cooking")
    print("her latest hobby is:", (Mariah_Carey["hobbies"][-1]))
    menu()
    return None

def seq6():
    """ get  print birthday a tuple with 3 numbers"""
    a = [int(Mariah_Carey["birth_date"][0:2]), int(Mariah_Carey["birth_date"][3:5]), int(Mariah_Carey["birth_date"][6:])]
    print("her BD in tuple 3 numbers:", tuple(a))
    menu()
    return None

def seq7():
    """ get  print how many hobbies she has"""
    Mariah_Carey["age"] = 35
    print("added her age:", Mariah_Carey["age"])
    menu()
    return None

def seq8():
    """exit"""
    print("Bye! it was fun")
    return None

Mariah_Carey = {"first_name" : "Mariah", "last_name" : "Carey",
 "birth_date" : "27.03.1970", "hobbies" : ["Sing", "Compose", "Act"]}

menu()







