"""Problem 74: Sine series."""

import math
x=float(input("Enter x in radians: "))
terms=int(input("Number of terms: "))
total=0
for i in range(max(0,terms)):
    power=2*i+1
    term=x**power/math.factorial(power)
    total += term if i%2==0 else -term
print("Sine series sum:",total)
