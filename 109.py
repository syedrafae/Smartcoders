"""Problem 109: X pattern."""

n=int(input("Size of X: "))
for i in range(n):
    for j in range(n):
        print("*" if i==j or i+j==n-1 else " ",end=" ")
    print()
