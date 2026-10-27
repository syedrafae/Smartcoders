"""Problem 29: Valid triangle."""

a,b,c=map(float,input("Enter three sides: ").split())
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a: print("Valid triangle")
else: print("Invalid triangle")
