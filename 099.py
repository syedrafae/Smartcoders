"""Problem 99: Alphabet sequential triangle."""

n=int(input("Number of rows (up to 26): "))
for i in range(1,min(n,26)+1): print(" ".join(chr(65+j) for j in range(i)))
