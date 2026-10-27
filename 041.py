"""Problem 41: Clock angle."""

hour=int(input("Hour (1-12): "))
minute=int(input("Minute (0-59): "))
if not 1<=hour<=12 or not 0<=minute<60: print("Invalid time")
else:
    h=(hour%12)*30+minute*0.5
    m=minute*6
    angle=abs(h-m)
    print("Smaller angle:", min(angle,360-angle), "degrees")
