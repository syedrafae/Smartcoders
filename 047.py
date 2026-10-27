"""Problem 47: Sum of natural numbers."""

n=int(input("Enter N: "))
print("Sum:", n*(n+1)//2 if n>=0 else "N must be non-negative")
