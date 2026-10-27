"""Problem 4: Temperature conversion."""

choice=input("Convert from (C)elsius or (F)ahrenheit? ").strip().upper()
if choice == "C":
    c=float(input("Celsius: "))
    print("Fahrenheit:", c*9/5+32)
elif choice == "F":
    f=float(input("Fahrenheit: "))
    print("Celsius:", (f-32)*5/9)
else:
    print("Invalid choice")
