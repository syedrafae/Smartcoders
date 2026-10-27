"""Problem 108: Right arrow pattern."""

n=int(input("Arrow height (odd recommended): "))
mid=n//2
for i in range(n):
    stars=i+1 if i<=mid else n-i
    print("*"+" "*(max(0,stars-1))+"*"*(max(0,stars-1)))
