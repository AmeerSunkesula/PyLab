#Find the Factorial of a given number using Function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#Main part of the program
input_value = int(input("Enter a number to find its factorial: "))

try:
    num=int(input_value)
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        fact = factorial(num)
        print(f"The factorial of {num} is {fact}.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")        