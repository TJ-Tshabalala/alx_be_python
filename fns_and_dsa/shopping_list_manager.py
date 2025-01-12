def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4 Exit")

def main():
    shopping_list = [] # Empty list
    while True:
        display_menu()
        choice = int(input("Enter the item to add: "))
        if choice == 1:
            item = input("Add the item: ")
            shopping_list.append(item)
            pass
        elif choice == 2:
            item = input("Remove an item: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("This item is not in the shopping list.")
                pass  
        elif choice == 3:
            for item in shopping_list:
                print(item)
                pass
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.") 

if __name__ == "__main__":
    main() 

