#n = int(input("N = "))

# def printName(n):
#     if n == 0:
#         return
#     print("s")
#     printName(n-1)
# printName(n)

# def printBack(i,n):
#     if (i>n):
#         return
#     print(i)
#     printBack(i+1,n)
#     print(i)
# i=1
# printBack(i,n)

# sum = 0
# def printSum(n, sum):
#     if (n<=0):
#         print(sum)
#         return
#     printSum(n-1, sum+n)
# printSum(n,sum)


# def printSumF(n):
#     if (n == 1):
#         return 1
#     return n + printSumF(n-1)

# print(printSumF(n))

# def factN(n):
#     if n == 1:
#         return 1
#     return n * factN(n-1)
# print(factN(n))

arr = [1,2,3,4,5,6]

# def reverse(i,n):
#     if i>n/2:
#         print(arr)
#         return
#     arr[i+1],arr [n-(i+1)] = arr [n-(i+1)], arr [i+1]
#     return reverse(i+1,n)
# reverse(0,n)
    
    
# s = "madam"
# def palind(i,n,s):
#     if (i>n/2):
#         return True
#     if s[i]==s[n-i-1]:
#         return palind(i+1, n, s)
#     else:
#         return False
# print(palind(0,len(s),s))
    
# 0,1,1,2,3,5,8

# def fibNfor(n):
#     f1 = 0
#     f2 = 1
#     f = 0
#     if n == 0:
#         return 0
#     elif n == 1:
#         return f1
#     else:
#         for i in range(1,n):
#             f = f2 + f1
#             f1 = f2
#             f2 = f           
#         return f
# print(fibNfor(4))

# def fibRec(n):
#     if n<=1:
#         return n
#     return fibRec(n-1) + fibRec(n-2)
# print(fibRec(5))
# TC : 2**N
