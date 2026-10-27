"""Problem 67: Armstrong number any digits."""

n=int(input("Enter integer: "))
digits=str(abs(n)); power=len(digits)
total=sum(int(d)**power for d in digits)
print("Armstrong number" if total==abs(n) else "Not an Armstrong number")
