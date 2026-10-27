"""Problem 82: Centered pyramid."""

n=int(input("Number of rows: "))
for i in range(1,n+1): print(" "*(n-i)+"*"*(2*i-1))
