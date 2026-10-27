"""Problem 97: Binary number triangle."""

n=int(input("Number of rows: "))
for i in range(1,n+1): print(" ".join(str(j%2) for j in range(i)))
