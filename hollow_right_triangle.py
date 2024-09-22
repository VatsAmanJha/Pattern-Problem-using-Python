n = int(input("Enter No. of side in Square:"))
for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):
        if j<=i:
            if j==i or j==1 or i==n:
                print("*",end="")
            else:
                print(" ",end="")
        else:
            print(" ", end="")
    print()
