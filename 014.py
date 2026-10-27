"""Problem 14: Check Kth bit."""

n=int(input("Enter number: "))
k=int(input("Enter bit position K (starting from 0): "))
if n & (1 << k): print("Kth bit is set")
else: print("Kth bit is not set")
