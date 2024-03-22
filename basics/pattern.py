# Things to remember
# 1. For the outer loop, count the number of lines
# 2. For the inner loop, focus on the columns and try to connect them to rows
# 3. Print them as *
# 4. Observe for symmetry 


def pattern7(num):
    n = num#input("enter number of lines")
    for i in range(0,n):
        for j in range(0, n-1-i):
            print(" ",end="")
        for j in range(0,2*i+1):
            print("*",end="")
        for j in range(0,n-1-i):
            print(" ",end="")
        print()

if __name__ == "__main__":
    n = 5
    pattern7(n)