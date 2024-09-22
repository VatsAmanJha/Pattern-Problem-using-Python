n = int(input("Enter No. of side in Square:"))
for i in range(1,n+1):
    for j in range(1,n*2):
        if j>=((n+1)-i) and j<=((n-1)+i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
