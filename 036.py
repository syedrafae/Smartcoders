"""Problem 36: Profit or loss."""

cp=float(input("Cost price: "))
sp=float(input("Selling price: "))
if sp>cp: print("Profit:", sp-cp)
elif cp>sp: print("Loss:", cp-sp)
else: print("No profit, no loss")
