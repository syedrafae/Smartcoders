"""Problem 31: Days in month."""

import calendar
m=int(input("Enter month (1-12): "))
if 1<=m<=12: print("Days:", calendar.monthrange(2024,m)[1])
else: print("Invalid month")
# 2024 is a leap year, so February has 29 days.
