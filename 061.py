"""Problem 61: Harmonic series sum."""

n=int(input("Enter N: "))
if n<=0: print("N must be positive")
else: print("Sum:", sum(1/i for i in range(1,n+1)))
