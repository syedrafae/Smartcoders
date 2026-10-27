"""Problem 21: Ticket pricing."""

age=int(input("Enter age: "))
if age<0: print("Invalid age")
elif age<5: price=0
elif age<=12: price=100
elif age<=59: price=200
else: price=120
print("Ticket price:", price)
# Example pricing rules: under 5 free, 5-12 ₹100, 13-59 ₹200, 60+ ₹120.
