n = int(input("Enter No. of side in Square:"))
for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):
        if i == 1 or i == n or j == 1 or j == n or j == i or j == (n+1)-i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
