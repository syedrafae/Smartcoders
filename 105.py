"""Problem 105: Number diamond."""

n=int(input("Half-height: "))
for i in range(1,n+1): print(" "*(n-i)+"".join(str(j) for j in range(1,i+1))+"".join(str(j) for j in range(i-1,0,-1)))
for i in range(n-1,0,-1): print(" "*(n-i)+"".join(str(j) for j in range(1,i+1))+"".join(str(j) for j in range(i-1,0,-1)))
