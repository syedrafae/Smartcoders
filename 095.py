"""Problem 95: Column-wise incrementing."""

n=int(input("Number of rows: "))
for i in range(1,n+1): print(" ".join(str(j) for j in range(1,i+1)))
