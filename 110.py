"""Problem 110: Plus pattern."""

n=int(input("Size (odd number recommended): "))
mid=n//2
for i in range(n):
    for j in range(n):
        print("*" if i==mid or j==mid else " ",end=" ")
    print()
