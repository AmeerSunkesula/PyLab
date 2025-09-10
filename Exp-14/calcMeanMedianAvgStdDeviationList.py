# Program to calculate mean, median, average and standard deviation of numbers in a list.
import statistics
def calculate_average(numbers):
    # Calculate the average of the numbers in the list
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    # Main function to calculate various statistical measures 
    print("Enter numbers separated by spaces:")
    try:
        #Input list of numbers
        # Split the input string into individual number strings and convert them to float, storing them in a list
        numbers = list(map(float, input().split()))
        if not numbers:
            print("The list is empty. Please enter some numbers.")
            return
        
        #Calculate statistical measures
        average=calculate_average(numbers)
        mean=statistics.mean(numbers)
        median=statistics.median(numbers)
        std_dev=statistics.stdev(numbers) if len(numbers) > 1 else 0.0
        
        #Display results
        print(f"\nNumbers: {numbers}")
        print(f"Average: {average}")
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Standard Deviation: {std_dev}")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
#Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    main()