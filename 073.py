"""Problem 73: Count and average until -1."""

count=0; total=0
while True:
    n=float(input("Enter a number (-1 to stop): "))
    if n==-1: break
    count+=1; total+=n
if count: print("Count:",count,"Average:",total/count)
else: print("No numbers entered")
