"""Problem 34: Quadratic roots."""

import math
a=float(input("Coefficient a: "))
b=float(input("Coefficient b: "))
c=float(input("Coefficient c: "))
if a==0:
    if b!=0: print("Linear root:", -c/b)
    else: print("Not a quadratic equation")
else:
    d=b*b-4*a*c
    if d>0:
        print("Two real roots:", (-b+math.sqrt(d))/(2*a), (-b-math.sqrt(d))/(2*a))
    elif d==0: print("Equal real roots:", -b/(2*a))
    else:
        real=-b/(2*a); imag=math.sqrt(-d)/(2*a)
        print("Imaginary roots:", complex(real,imag), complex(real,-imag))
