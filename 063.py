"""Problem 63: Power without pow."""

x=float(input("Enter x: "))
n=int(input("Enter non-negative exponent n: "))
if n<0: print("Please enter n >= 0")
else:
    result=1
    for _ in range(n): result*=x
    print("x^n =", result)
