"""Problem 20: Vowel or consonant."""

ch=input("Enter a letter: ").lower()
if len(ch)==1 and ch.isalpha():
    if ch in "aeiou": print("Vowel")
    else: print("Consonant")
else: print("Enter one alphabet character")
