n = 3#input("enter number of lines")
for i in range(0,n):
    for j in range(0, i):
        print(" ",end="")
    for j in range(0,2*(n-i)-1):
        print("*",end="")
    for j in range(0,i):
        print(" ",end="")
    print()

