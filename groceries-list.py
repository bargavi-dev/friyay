#Ask user what they want to do: Add, print, or remove
groceries_list = []

while True:

    action = input('Do you want to add, print, or remove an item? ').lower()
    if action == "add":
        add2 = "yes"
        while add2 == "yes":
            item = input('What would you like to add? ')
            groceries_list.append(item)
            add2 = input('Add another? ').lower()
            if add2 != "yes" and add2 != "no":
                print('Please try again')


    elif action == "print":
        print("\nGrocery List: ")
        for index in range(len(groceries_list)):
            print(f'{index + 1}: {groceries_list[index].capitalize()}')
    elif action == "remove":
        remove2 = "yes"
        while remove2 == "yes":
            remove1 = input('What would you like to remove? ')
            groceries_list.remove(remove1)
            remove2 = input('Remove another? ').lower()
            if remove2 != "yes" and remove2 != "no":
                print('Please try again')
    else: 
        print('Please try again')






#Add: accept input, ask "add another", if no then go back to main menu

#Print:print the list nicely with numbers

#Remove: "which item?", remove item, ask "remove another?", if no then back to main menu