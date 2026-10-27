"""Problem 96: Reverse number triangle."""

n=int(input("Number of rows: "))
for i in range(n,0,-1): print(" ".join(str(j) for j in range(i,0,-1)))
