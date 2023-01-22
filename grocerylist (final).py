import sys


def main():
    """
    write a shopping list program
    begin by inputing a display menu for the user (done)
    give the display menu 4 instructions
    1. add item (done)
    2. list item (done)
    3. remove item (done)
    4. quit 
    the program shown when ran will depend on customer selection
    """


    grocery_list = []
    choice = display_menu()

    while choice != 4:
        if choice == 1:
            grocery_list = add_item(grocery_list)
            choice = display_menu()
        elif choice == 2:
            display_list(grocery_list)
            choice = display_menu()
        elif choice == 3:
            grocery_list = delete_item(grocery_list)
            choice = display_menu()
    sys.exit("Exiting Menu...")
         

def display_menu():
    message = "1. add item\n2. list item\n3. remove item\n4. quit\n> "
    valid_options = [1, 2, 3, 4]
    choice = 0
    
    while choice not in valid_options:
        try:
            choice = int(input(message))
        except ValueError:
            print("Please enter a valid option [1-4]")
            continue
    return choice


def add_item(item_list):
    # ask a user what item to be add
    # returns that updated list 
    item = input("item to be added: ")
    item = item.lower() 
    if item not in (item_list):
        item_list.append(item)
    else:
        print(f"{item}: already exist")
    return item_list


def display_list(item_list):
    if len(item_list) != 0:
        for item in item_list:
            print(item, end=" ")
        print()


def delete_item(item_list):
    item = input("item to be deleted: ")
    if item in item_list:
        item_list.remove(item)
    return item_list
    

 
if __name__ == '__main__':
    main()