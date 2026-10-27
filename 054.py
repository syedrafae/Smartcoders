"""Problem 54: Digits left to right."""

n=input("Enter a non-negative integer: ").strip()
if n.isdigit():
    print("Digits from left to right:")
    for digit in n: print(digit)
else: print("Invalid integer")
