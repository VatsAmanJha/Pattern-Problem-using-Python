for i in range(1,4):
    for j in range(1,20):
        if j<10:
            if j>=(4-i) and j<=(6+i):
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
        elif j>10:
            if j>=(14-i) and j<=(16+i):
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(1,11):
    for j in range(1,20):
        if j>=i and j<=(20)-i:
            print("❤️",end=" ")
        else:
            print(" ",end=" ")
    print()
