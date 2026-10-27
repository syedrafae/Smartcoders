"""Problem 68: Largest and smallest digit."""

n=abs(int(input("Enter integer: ")))
digits=[int(d) for d in str(n)]
print("Largest digit:",max(digits))
print("Smallest digit:",min(digits))
