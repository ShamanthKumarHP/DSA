n = 50
prime = ['2','3','5','7']
even = ['0','2','4','6','8']
'''
Analysis
for n = 5   _ _ _ _ _ 
i will be having 5 place, in which 3 are even and 2 are odd. i can get this by formula
for even = (n+1)/2
for odd = (n)/2

so, 
for a even position i can put any 5 elements from "even" list
for a odd position i can put any 4 elements from "odd" list

for n = 2, there will be 1 even and 1 odd position, so 
ans = 5 * 4


the general formula will be
(5 ** number of even place )  * ( 4 ** number of odd places)

Note: Apply mod immediately after getting a ans. Dont wait for last answer. this will reduce TC and SC

'''
mod = 10 ** 9 + 7
def findPower(base, power):
    if power == 0:
        return 1
    if power % 2 == 0:
        ans = findPower(base, power/2)
        ans = ans % mod
        return (ans * ans) % mod
    else:
        ans = base * findPower(base, power-1)
    return ans

def countGoodnumbers(n):
    even_places = int((n+1)/2)
    odd_places = int(n/2)
    even_value = findPower(5, even_places)
    odd_value = findPower(4, odd_places)
    ans = (even_value * odd_value) % mod
    return  ans

print(countGoodnumbers(50))