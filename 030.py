"""Problem 30: Simple calculator."""

a=float(input("First number: "))
op=input("Operator (+, -, *, /): ")
b=float(input("Second number: "))
if op=="+": print(a+b)
elif op=="-": print(a-b)
elif op=="*": print(a*b)
elif op=="/":
    if b!=0: print(a/b)
    else: print("Cannot divide by zero")
else: print("Invalid operator")
