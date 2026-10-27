"""Problem 83: Inverted pyramid."""

n=int(input("Number of rows: "))
for i in range(n,0,-1): print(" "*(n-i)+"*"*(2*i-1))
