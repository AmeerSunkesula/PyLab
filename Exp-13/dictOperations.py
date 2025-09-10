#Program to Manage operations on a dictionary: create, add, delete, and display elements
def create_dictionary():
    # Create a new empty dictionary
    print("A new dictionary has been created!")
    return {}

def add_element_to_dict(dct):
    # Add a key-value pair to the dictionary
    key = input("Enter the key to add: ")
    value = input("Enter the value for the key: ")
    dct[key] = value
    print(f"Key-Value pair ({key}: {value}) added to the dictionary.")

def delete_element_from_dict(dct):
    # Delete a key-value pair from the dictionary
    if not dct:
        print("The dictionary is empty, nothing to delete.")
        return
    key = input("Enter the key to delete: ")
    if key in dct:
        del dct[key]
        print(f"Key '{key}' has been removed from the dictionary.")
    else:
        print(f"Key '{key}' not found in the dictionary.")

def display_dictionary(dct):
    # Display the elements of the dictionary
    if not dct:
        print("The dictionary is empty.")
    else:
        print("Current Dictionary:", dct)

def main():
    # Main function to demonstrate dictionary operations
    my_dict = create_dictionary()
    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Add a new element to the dictionary")
        print("2. Delete an element from the dictionary")
        print("3. Display the dictionary")
        print("4. Exit")

        # take user input
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_element_to_dict(my_dict)
        elif choice == '2':
            delete_element_from_dict(my_dict)
        elif choice == '3':
            display_dictionary(my_dict)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")
#Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    main()