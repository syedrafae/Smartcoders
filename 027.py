"""Problem 27: Electricity bill."""

units=float(input("Enter electricity units: "))
if units<0: print("Invalid units")
else:
    # Practice slab rates: first 100 at ₹1.5/unit, next 100 at ₹2.5, rest at ₹4.
    if units<=100: bill=units*1.5
    elif units<=200: bill=100*1.5+(units-100)*2.5
    else: bill=100*1.5+100*2.5+(units-200)*4
    print("Electricity bill: ₹", bill)
