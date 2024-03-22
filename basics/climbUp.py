def climb(n):
    if n <=2:
        return n
    else:
        return climb(n-1)+climb(n-2)

n = 5
print(climb(4))