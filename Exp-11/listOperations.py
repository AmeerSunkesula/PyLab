#Program to Manage a list with add delete and display operations
def display_menu():
    print("\n Menu:")
    print("1. Create a list")
    print("2. Add an element")
    print("3. Delete an element")
    print("4. Display the list")
    print("5. Exit")
def create_list():
    # Create a new empty list
    print("New list created successfully.")
    return []
def add_element(lst):
    # Add an element to the list
    element = input("Enter the element to add: ")
    lst.append(element)
    print(f"{element}' added to the list.")
def delete_element(lst):
    # Delete an element from the list
    element = input("Enter the element to delete: ")
    if not lst:
        print("The List is empty, nothing to Delete.")
        return
    try:
        element=input("Enter the element to delete: ")
        lst.remove(element)
        print(f"{element} has been removed from the list.")
    except ValueError:
        print(f"{element} not found in the list.")
def display_list(lst):
    # Display the elements of the list
    if not lst:
        print("The List is empty.")
    else:
        print("Current List:", lst)
def main():
    # Main function to handle user inputs and operations 
    user_list = create_list()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            user_list = create_list()
        elif choice == '2':
            add_element(user_list)
        elif choice == '3':
            delete_element(user_list)
        elif choice == '4':
            display_list(user_list)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
#Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    main()