"""Problem 92: Pascal triangle."""

n=int(input("Number of rows: "))
for i in range(n):
    value=1
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print(value,end=" ")
        value=value*(i-j)//(j+1) if j<i else 1
    print()
