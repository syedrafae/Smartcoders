"""Problem 98: Alphabet triangle row repeat."""

n=int(input("Number of rows (up to 26): "))
for i in range(1,min(n,26)+1): print(" ".join([chr(64+i)]*i))
