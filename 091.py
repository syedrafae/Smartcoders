"""Problem 91: 1-0 alternating triangle."""

n=int(input("Number of rows: "))
for i in range(1,n+1):
    print(" ".join(str(1 if j%2==0 else 0) for j in range(i)))
