"""Problem 52: Happy number."""

n=int(input("Enter a positive integer: "))
seen=set()
while n!=1 and n not in seen:
    seen.add(n)
    total=0
    for digit in str(abs(n)): total+=int(digit)**2
    n=total
print("Happy number" if n==1 else "Not a happy number")
