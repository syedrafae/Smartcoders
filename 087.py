"""Problem 87: Sandglass."""

n=int(input("Half-height: "))
for i in range(n,0,-1): print(" "*(n-i)+"*"*(2*i-1))
for i in range(2,n+1): print(" "*(n-i)+"*"*(2*i-1))
