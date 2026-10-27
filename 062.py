"""Problem 62: Alternating signed sum."""

n=int(input("Enter N: "))
total=0
for i in range(1,n+1):
    total += i if i%2 else -i
print("Sum:", total)
