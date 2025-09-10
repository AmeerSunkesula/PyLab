#Generate multiplication table from 1 to 10 for numbers 1 to 5
for num in range(1,6):
    print(f"Multiplication table for {num}:")
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
    print()  # Print a blank line after each tableS