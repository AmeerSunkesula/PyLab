bits=int(input("Enter the number of bits: "))

#Conversion factors
bytes_value = bits / 8
kilobytes= bytes_value / 1024
megabytes = kilobytes / 1024
gigabytes = megabytes / 1024
terabytes = gigabytes / 1024

#Output with formatting
print(f"{bits} bits is equal to:")
print(f"{bytes_value:.2f} Bytes")
print(f"{kilobytes:.2f} KB")
print(f"{megabytes:.4f} MB")
print(f"{gigabytes:.6f} GB")
print(f"{terabytes:.9f} TB")