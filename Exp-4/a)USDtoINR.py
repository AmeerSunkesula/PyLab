conversion_rate = 88.11 # 1 USD = 88.11 INR(as of 2025-08-15)
usd=float(input("Enter amount in U.S. Dollars : "))
inr=usd*conversion_rate
print(f"{usd} U.S. Dollars is equal to {inr} Indian rupees.")