"""Problem 22: Age category."""

age=int(input("Enter age: "))
if age<0: print("Invalid age")
elif age<=12: print("Child")
elif age<=19: print("Teenager")
elif age<60: print("Adult")
else: print("Senior")
