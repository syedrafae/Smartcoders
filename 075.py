"""Problem 75: String palindrome using recursion."""

def palindrome(s):
    if len(s)<=1: return True
    if s[0]!=s[-1]: return False
    return palindrome(s[1:-1])
text=input("Enter a string: ")
clean="".join(ch.lower() for ch in text if ch.isalnum())
print("Palindrome" if palindrome(clean) else "Not a palindrome")
