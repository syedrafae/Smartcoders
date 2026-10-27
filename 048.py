"""Problem 48: Count digits."""

n=abs(int(input("Enter integer: ")))
count=1 if n==0 else 0
while n>0:
    count+=1
    n//=10
print("Digits:", count)
