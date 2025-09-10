# Program to manage operations on a list: sort, reverse, and count elements
def sort_list(lst):
    # Sort the list in ascending order
    lst.sort()
    print("Sorted list:", lst)
def reverse_list(lst):
    # Reverse the order of elements in the list
    lst.reverse()
    print("Reversed list:", lst)
def count_element(lst):
    # Count the total number of elements in the list
    count = len(lst)
    print("Total number of elements in the list:", count)
def main():
    # Main function to handle user inputs and operations 
    # Example list for demonstration
    my_list = [5, 2, 9, 1, 5, 6]
    print("Original list:", my_list)
    
    #Sort the list
    sort_list(my_list)
    
    #Reverse the list
    reverse_list(my_list)

    #Counting elements in the list
    count_element(my_list)
#Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    main()