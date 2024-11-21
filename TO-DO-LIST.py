user_input = "random"
data =[]

def show_menu():
    print("Menu:")
    print("1.add an item")
    print("2. Mark as done")
    print("3.view item")
    print("4.Exit")

while user_input !='4':

    show_menu()
    user_input = input("Enter your choice: ")

    if user_input =='1':
        item = input("what to be done?")
        data.append(item)
        print('Added item',item)
    elif user_input =='2':
        item = input("what is to be marked as done?")
        if item in data:
            data.remove(item)
            print("Removed item",item)
        else:
            print("item does not exit in the list")
    elif user_input =='3':
        print("List of to-do items:")
        for item in data:
            print(item)
    elif user_input =='4':
        print("Exit")
    else:
        print(" Please choose a valid option.")