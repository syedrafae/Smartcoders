"""Problem 42: Scholarship eligibility."""

marks=float(input("Marks percentage: "))
attendance=float(input("Attendance percentage: "))
income=float(input("Family annual income: "))
# Practice criteria: marks >= 85, attendance >= 90%, income <= ₹300000.
if marks>=85 and attendance>=90 and income<=300000: print("Eligible for scholarship")
else: print("Not eligible for scholarship")
