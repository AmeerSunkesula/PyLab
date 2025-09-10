#Take two numbers as input and perform simple arithmetic operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#Performing arithmetic operations
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2
exponentiation = num1 ** num2
floor_division = num1 // num2

#Displaying the results
print(f"Sum: {num1} + {num2} = {sum}")
print(f"Difference: {num1} - {num2} = {difference}")
print(f"Product: {num1} * {num2} = {product}")
print(f"Quotient: {num1} / {num2} = {quotient}")
print(f"Remainder: {num1} % {num2} = {remainder}")
print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")
print(f"Floor Division: {num1} // {num2} = {floor_division}")