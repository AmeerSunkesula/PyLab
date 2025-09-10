#Generate Multiplication table from 1 to 10 for numbers 1 to 5 using functions
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print()  # Print a newline for better readability

#Main program
for num in range(1, 6):
    multiplication_table(num)