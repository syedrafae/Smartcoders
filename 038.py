"""Problem 38: Three-digit Armstrong number."""

n=int(input("Enter a three-digit number: "))
if 100<=abs(n)<=999:
    s=str(abs(n))
    total=sum(int(d)**3 for d in s)
    if total==abs(n): print("Armstrong number")
    else: print("Not an Armstrong number")
else: print("Please enter a three-digit number")
