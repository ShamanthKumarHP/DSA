def recursion(arr):
    def partitioning(i,j):
        if i == j :
            return 0 # 0 number of x operations
        
        mini = int(1e9)
        for k in range(i,j):
            steps = arr[i-1] * arr[k] * arr[j] + partitioning(i,k) + partitioning(k+1,j)
            mini = min(steps, mini)

        return mini 
    return partitioning(1, len(arr)-1)


def memo(arr):
    def partitioning(i,j, dp):
        if i == j :
            return 0 # 0 number of x operations
    
        if dp[i][j] != -1:
            return dp[i][j]
        
        mini = int(1e9)
        for k in range(i,j):
            steps = arr[i-1] * arr[k] * arr[j] + partitioning(i,k, dp) + partitioning(k+1,j, dp)
            mini = min(steps, mini)

        dp[i][j] = mini
        return dp[i][j] 
    
    dp = [ [-1 for i in range(len(arr))] for j in range(len(arr))]
    return partitioning(1, len(arr)-1, dp)


def tabu(arr):
    n = len(arr)
    dp = [ [0 for i in range(n)] for j in range(n)]

    # bc
    for i in range(1, n):
        # i == j
        dp[i][i] = 0

    # run loop from n-1 to 1  -> i
        # run loop from i+1 to n-1   -> j
        # why i + 1, because we start from 1. func(1, N-1)

    for i in range(n-1, 0, -1):
        for j in range(i+1, n):
            mini = int(1e9)
            for k in range(i,j):
                steps = arr[i-1] * arr[k] * arr[j] + dp[i][k] + dp[k+1][j]
                mini = min(steps, mini)
            dp[i][j] = mini
    print(dp)
    return dp[1][n-1]


#     #[     A,  B,  C,  D]
arr = [10, 20, 30, 40,50]

# arr = [60,50,10,60]

print(recursion(arr))
print(memo(arr))
print(tabu(arr))