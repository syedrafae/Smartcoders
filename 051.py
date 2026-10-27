"""Problem 51: Number palindrome."""

n=int(input("Enter integer: "))
s=str(abs(n))
if s==s[::-1]: print("Palindrome")
else: print("Not a palindrome")
