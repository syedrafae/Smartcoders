"""Problem 104: Hollow diamond inside rectangle."""

n=int(input("Half-height: "))
for i in range(1,n+1):
    print("*"*i+" "*(2*n-2*i)+"*"*i)
for i in range(n-1,0,-1):
    print("*"*i+" "*(2*n-2*i)+"*"*i)
