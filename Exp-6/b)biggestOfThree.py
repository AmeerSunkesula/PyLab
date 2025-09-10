#Finding the biggest of three numbers
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
num3=float(input("Enter third number: "))
greatest=num1 if (num1>num2 and num1>num3) else (num2 if num2>num3 else num3)
print(f"The greatest number is: {greatest}")