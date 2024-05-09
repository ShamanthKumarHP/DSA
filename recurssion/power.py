# NOTE power
x = 2
n = 3
def calculatePower(x,n):
    if n == 0:
        return 1
    return x * calculatePower(x,n-1)

def calculate_power(x,n):
    if n == 0:
        return 1
    temp = calculate_power(x,int(n/2))
    ans = temp * temp

    if n%2!=0:
        ans = ans*x
    return ans

print(calculatePower(x,n))
print(calculate_power(x,n))

# maximum recursion depth will exceed if its not logN
def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / (x * myPow(x, -n -1))
    elif n%2 == 0:
        a = myPow(x, n//2)
        return a*a
    return x * myPow(x, n-1)