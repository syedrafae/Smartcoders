"""Problem 40: ATM withdrawal."""

balance=float(input("Account balance: "))
amount=float(input("Withdrawal amount: "))
minimum=float(input("Minimum balance to keep: "))
if amount<=0: print("Invalid withdrawal amount")
elif amount>balance: print("Rejected: insufficient funds")
elif balance-amount<minimum: print("Rejected: minimum balance rule")
else: print("Approved. Remaining balance:", balance-amount)
