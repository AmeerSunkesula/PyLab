#Find the factorial of a Given number using Recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1) #Recursive Call
    
#Main Part of the program
input_value=int(input("Enter a number to find its factorial: "))
try:
    num=int(input_value)
    if num<0:
        print("Factorial is not defined for negative numbers")
    else:
        print(f"The factorial of {num} is {factorial(num)}")
except ValueError:
    print("Please enter a valid number")        