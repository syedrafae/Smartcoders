"""Problem 55: Factorial."""

n=int(input("Enter N: "))
if n<0: print("Factorial is not defined for negative integers")
else:
    fact=1
    for i in range(1,n+1): fact*=i
    print("Factorial:", fact)
