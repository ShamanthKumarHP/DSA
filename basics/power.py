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