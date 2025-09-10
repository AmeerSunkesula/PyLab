#Taking Input from user and converting it to different data types
num_str = input("Enter a number: ")
print("\nData Type Conversion")

#Converting string input to integer
num_int = int(num_str)
print(f"String to Integer: {num_str} -> {num_int})")

#Converting string input to float
num_float = float(num_str)
print(f"String to Float: {num_str} -> {num_float})")

#Converting integer to float
int_to_float = float(num_int)
print(f"Integer to Float: {num_int} -> {int_to_float})")

#Converting float to integer
float_to_int = int(num_float)
print(f"Float to Integer: {num_float} -> {float_to_int})")

#Converting integer to string
int_to_str = str(num_int)
print(f"Integer to String: {num_int} -> {int_to_str})")

#Converting float to string
float_to_str = str(num_float)
print(f"Float to String: {num_float} -> {float_to_str})")

#Convert integer to boolean(Empty string is False, any other Number is True)
int_to_bool = bool(num_int)
print(f"Integer to Boolean: {num_int} -> {int_to_bool})")

#Convert string to boolean(Empty string is False, any other string is True)
str_to_bool = bool(num_str)
print(f"String to Boolean: '{num_str}' -> {str_to_bool})")