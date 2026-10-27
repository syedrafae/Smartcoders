"""Problem 90: Floyd's triangle."""

n=int(input("Number of rows: "))
value=1
for i in range(1,n+1):
    for _ in range(i):
        print(value,end=" ")
        value+=1
    print()
