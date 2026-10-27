"""Problem 100: Reverse alphabet triangle."""

n=int(input("Number of rows (up to 26): "))
for i in range(min(n,26),0,-1): print(" ".join(chr(64+j) for j in range(1,i+1)))
