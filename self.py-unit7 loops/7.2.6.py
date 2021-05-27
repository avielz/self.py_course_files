
#Milk,Cottage,Tomatoes

def note() :
    """Function gets a string with grocery items seperated by commas with no spaces and one number with a value between 1 and 9. depending on the number Ition will
    1 -print the item list
    2- print the number of items on the list
    3- enter an item name and I will answer if its on the list
    4- enter an item name and I will answer how many times it appears
    5- enter an item name and I will erase the item once
    6- enter an item name and I will add the item to the list
    7- print all illegal items (item length < 3 or with characters that aren't letters)
    8- remove all repeating items
    9- exit
    after the run the user is returned to the main menu again until choosing 9 to exit.

    *guideline move the items string into a list
    """
    return None

def seq1(grocery_list):
    print(grocery_list)
    menu(grocery_list)
    return None

def seq2(grocery_list):
    print("Items on the list: ", len(grocery_list))
    menu(grocery_list)
    return None

def seq3(grocery_list):
    requested_item = input("Enter item name: ")
    if requested_item in grocery_list :
        print(requested_item, " is on the list!")
    else : print("Sorry ", requested_item, "is not on the list.")
    menu(grocery_list)
    return None

def seq4(grocery_list):
    requested_item = input("Enter item name: ")
    result = grocery_list.count(requested_item)
    if result > 0 :
         print(requested_item, "appears", result, "time on the list")
    else: print("Sorry ", requested_item, "is not on the list.")
    menu(grocery_list)
    return None

def seq5(grocery_list):
    item_to_delete = input("Enter item to delete once from the list: ")
    if item_to_delete in grocery_list :
        grocery_list.remove(item_to_delete)
        print(item_to_delete, "has been removed from the list:", grocery_list)
    else: print("Sorry ", item_to_delete, "is not on the list.")
    menu(grocery_list)
    return None

def seq6(grocery_list):
    requested_item = input("Enter item name to add to the list: ")
    grocery_list.append(requested_item)
    print("I added", requested_item, "to the list:", grocery_list)
    menu(grocery_list)
    return None

def seq7(grocery_list):
    illegal_list =[]
    for item in grocery_list :
        if len(item) < 3 or not item.isalpha() :
            illegal_list.append(item)
    if len(illegal_list) > 0 :
        print("These are problematic items on the list:", illegal_list)
    else: print("No problematic items on the list!")          
    menu(grocery_list)
    return None

def seq8(grocery_list):
    #temp_grocery_list = grocery_list
    #temp_grocery_list = dict.fromkeys(temp_grocery_list)
    #a = list(temp_grocery_list)
    #grocery_list = a
    grocery_list = list(dict.fromkeys(grocery_list))
    print("I removed all the repeating items in the list: ", grocery_list)
    menu(grocery_list)
    return None

def seq9():
    print("Good bye!")
    return None

def menu(grocery_list) :
    """Print the menu list and get the number input.
     
    """
    menu_input = input("""
    Menu:
    1 -print the item list
    2- print the number of items on the list
    3- enter an item name and I will answer if its on the list
    4- enter an item name and I will answer how many times it appears
    5- enter an item name and I will erase the item once
    6- enter an item name and I will add the item to the list
    7- print all illegal items (item length < 3 or with characters that aren't letters)
    8- remove all repeating items
    9- exit

    Please Enter your selection: 
    """)
    if menu_input == "1" :
        seq1(grocery_list)
    elif menu_input == "2" :
         seq2(grocery_list)
    elif menu_input == "3" :
        seq3(grocery_list)
    elif menu_input == "4" :
        seq4(grocery_list)
    elif menu_input == "5" :
        seq5(grocery_list)
    elif menu_input == "6" :
         seq6(grocery_list)
    elif menu_input == "7" :
        seq7(grocery_list)
    elif menu_input == "8" :
        seq8(grocery_list)
    elif menu_input == "9" :
        seq9()
    else : 
        print("enter a valid option from 1-9")
        menu(grocery_list)
    return None

def main():
    menu(grocery_list)
    
grocery_string = input("Enter grocery items (separated by commas with no space): ")
grocery_list = grocery_string.split(",") #split string to item list

if __name__ == "__main__":
  main()


