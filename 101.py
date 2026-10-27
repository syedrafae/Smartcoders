"""Problem 101: Right-aligned alphabet triangle."""

n=int(input("Number of rows (up to 26): "))
for i in range(1,min(n,26)+1): print(" "*(n-i)+" ".join(chr(65+j) for j in range(i)))
