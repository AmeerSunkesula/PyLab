#Program to find the factors of a number
def print_factors(num):
    print(f"The factors of {num} are: ")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

#Main Part of the program
number=int(input("Enter a number to find its factors: "))
print_factors(number)