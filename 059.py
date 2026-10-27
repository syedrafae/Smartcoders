"""Problem 59: LCM."""

import math
a=int(input("First integer: "))
b=int(input("Second integer: "))
print("LCM:", abs(a*b)//math.gcd(a,b) if a and b else 0)
