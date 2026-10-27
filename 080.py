"""Problem 80: Right-aligned star triangle."""

n=int(input("Number of rows: "))
for i in range(1,n+1): print(" "*(n-i)+"*"*i)
