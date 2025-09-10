#Generate Fibonacci series upto 100 using recursion
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2) #Recursive Call

def print_fibonacci(limit):
    i=0
    while True:
        fib_num=fibonacci(i)
        if fib_num>limit:
            break
        print(fib_num, end=" ")
        i+=1
    print() #For newline after printing the series

#Main Part of the program
while True:
    input_value=input("Enter the maximum value for the Fibonacci sequence (or type 'exit' to quit): ")

    if input_value.lower()=='exit':
        print("Exiting the program.")
        break
    try:
        limit=int(input_value)
        if limit>=0:
            print(f"Fibonacci series up to {limit}:")
            print_fibonacci(limit)
            print()
        else:
            print("Please enter a non-negative integer.\n")
    except ValueError:
        print("Please enter a valid number.\n")