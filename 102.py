"""Problem 102: Alphabet pyramid."""

n=int(input("Number of rows (up to 26): "))
for i in range(1,min(n,26)+1):
    left=[chr(65+j) for j in range(i)]
    print(" "*(n-i)+" ".join(left+left[-2::-1]))
