"""Problem 106: Zigzag pattern."""

n=int(input("Number of stars per full row: "))
for _ in range(2): print("*"*n)
print(" "*(n//2)+"*")
for _ in range(2): print("*"*n)
