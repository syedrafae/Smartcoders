"""Problem 26: Day of week."""

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
n=int(input("Enter day number (1-7): "))
if 1<=n<=7: print(days[n-1])
else: print("Invalid day number")
