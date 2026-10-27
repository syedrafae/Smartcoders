"""Problem 39: Salary with overtime."""

hours=float(input("Hours worked: "))
rate=float(input("Hourly rate: "))
if hours<0 or rate<0: print("Invalid input")
elif hours>40: print("Salary:", 40*rate+(hours-40)*rate*1.5)
else: print("Salary:", hours*rate)
