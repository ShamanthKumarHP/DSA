# Tabulation -> Bottom - UP
# Memoization -> Top - Down

n = 6

# recussion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print("recussion", fibonacci(n))

# memoization 
def mem_fibonacci(n, dp):
    if n <= 1:
        return n    
    if dp[n] != -1:
        return dp[n]

    dp[n] = mem_fibonacci(n-1,dp) + mem_fibonacci(n-2,dp)
    return dp[n]

dp = [-1] * (n+1)
print("memoization", mem_fibonacci(n, dp))


# tabulation/ iterative
def tab_fibonacci(n):
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print("tabulation", tab_fibonacci(n))


# space optimization

def space_fibonacci(n):
    if n <= 1:
        return n
    prev2 = 0
    prev1 = 1
    for i in range(2,n+1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return curr

print("space_fibonacci", space_fibonacci(n))

