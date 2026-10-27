"""Problem 28: Triangle type."""

a,b,c=map(float,input("Enter three sides: ").split())
if a<=0 or b<=0 or c<=0: print("Invalid sides")
elif a==b==c: print("Equilateral triangle")
elif a==b or b==c or a==c: print("Isosceles triangle")
else: print("Scalene triangle")
