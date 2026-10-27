"""Problem 84: Diamond."""

n=int(input("Half-height of diamond: "))
for i in range(1,n+1): print(" "*(n-i)+"*"*(2*i-1))
for i in range(n-1,0,-1): print(" "*(n-i)+"*"*(2*i-1))
