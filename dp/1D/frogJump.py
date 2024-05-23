# https://takeuforward.org/data-structure/dynamic-programming-frog-jump-dp-3/

# Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair.
#  At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, 
# the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. 
# We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.


arr = [10,20,30,10]
arr = [10,40,10,20,100]

def recursion(idx):
    if idx == 0:
        return 0
    oneJump = abs(arr[idx] - arr[idx-1]) + recursion(idx-1)
    twoJump = float('inf')
    if (idx > 1):
        twoJump = abs(arr[idx] - arr[idx-2]) + recursion(idx-2)

    return min(oneJump, twoJump)

print("recursion", recursion(len(arr) - 1))

def memo(idx, ds):
    if idx == 0:
        return 0
    
    if ds[idx] != -1:
        return ds[idx]
    
    oneJump = abs(arr[idx] - arr[idx-1]) + memo(idx-1,ds)
    twoJump = float('inf')
    if (idx > 1):
        twoJump = abs(arr[idx] - arr[idx-2]) + memo(idx-2, ds)

    ds[idx] = min(oneJump, twoJump)
    return ds[idx]

ds = [-1] * (len(arr))
print("memo", memo(len(arr)-1, ds))
print(ds)
print()

def tabu1(n, dp):
    dp[0] = 0
    for i in range(1,n):
        oneJump = abs(arr[i] - arr[i-1]) + dp[i-1]
        twoJump = float('inf')
        twoJump = abs(arr[i] - arr[i-2]) + dp[i-2]
        dp[i] = min(oneJump, twoJump)
    return dp[-1]

# forming array theoreticaly 
# dp will contain the minimum cost required to go from i
#  choose path1, (current - prev1) and add dp[i-1]
#  choose path2, (current - prev2) and add dp[i-2]


def spacy(n):
    if n < 2:
        return 0
    prev1 = abs(arr[0] - arr[1])
    prev2 = 0
    for i in range(2,n):
        path1 = abs(arr[i] - arr[i-1]) + prev1
        path2 = abs(arr[i] - arr[i-2]) + prev2
        prev2 = prev1
        prev1 = min(path1, path2)
    return prev1

print("spacy", spacy(len(arr)))

