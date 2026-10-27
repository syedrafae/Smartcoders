"""Problem 37: Coordinate quadrant."""

x=float(input("x coordinate: "))
y=float(input("y coordinate: "))
if x==0 and y==0: print("Origin")
elif x==0: print("Y-axis")
elif y==0: print("X-axis")
elif x>0 and y>0: print("First quadrant")
elif x<0 and y>0: print("Second quadrant")
elif x<0 and y<0: print("Third quadrant")
else: print("Fourth quadrant")
