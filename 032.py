"""Problem 32: Sign then even or odd."""

n=int(input("Enter number: "))
if n>0:
    if n%2==0: print("Positive and even")
    else: print("Positive and odd")
elif n<0: print("Negative")
else: print("Zero")
