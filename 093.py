"""Problem 93: Centered number pyramid."""

n=int(input("Number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1): print(j,end=" ")
    print()
