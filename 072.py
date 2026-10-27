"""Problem 72: Binary to decimal."""

binary=input("Enter binary number: ").strip()
if binary and all(ch in "01" for ch in binary):
    decimal=0
    for bit in binary: decimal=decimal*2+int(bit)
    print("Decimal:",decimal)
else: print("Invalid binary number")
