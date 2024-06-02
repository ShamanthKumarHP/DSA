# https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

N = 3 # number of items
W = 4 # capacity of knapsack
values = [1,2,3] # items value
weights = [4,5,1] # weights of item
Output = 3

def rknapsack(N, W, values, weights):

    def recursion(idx, capacity):
        if idx == 0:
            if capacity >= weights[0]:
                return values[0]
            else:
                return 0
        
        notTake = 0 + recursion(idx-1, capacity)

        take = float('-inf')
        if weights[idx] <= capacity:
            take = values[idx] + recursion(idx-1, capacity - weights[idx])
        return max(take, notTake)
    return recursion(N-1, W)

def mknapsack(N, W, values, weights):
    dp = [[-1 for i in range(W+1)] for j in range(N)]

    def memo(idx, capacity):
        if idx == 0:
            if capacity >= weights[0]:
                return values[0]
            else:
                return 0
        
        if dp[idx][capacity]!= -1:
            return dp[idx][capacity]
        
        notTake = 0 + memo(idx-1, capacity)

        take = float('-inf')
        if weights[idx] <= capacity:
            take = values[idx] + memo(idx-1, capacity - weights[idx])

        dp[idx][capacity] = max(take, notTake)
        return dp[idx][capacity]
        
    ans = memo(N-1, W)
    return ans

def tknapsack(N, W, values, weights):
    def tabu():
        capacity = W
        dp = [[-1 for i in range(W+1)] for j in range(N)]

        # if i'm at index 0, i can steal only when i have capacity that is greater than or equal to the weights[0]
        for i in range(weights[0], capacity):
            dp[0][i] = dp[0][values[0]]
        
        for r in range(1, N):
            for c in range(W+1):
                # take
                notTake = dp[r-1][c]
                take = 0
                if weights[r] <= c:
                    take = values[r] + dp[r-1][c]
                dp[r][c] = max(take, notTake)
                
        return dp[-1][-1]
    return tabu()

def sknapsack(N, W, values, weights):
    def spacy():
        capacity = W
        prev = [-1 for i in range(W+1)]

        # if i'm at index 0, i can steal only when i have capacity that is greater than or equal to the weights[0]
        for i in range(weights[0], capacity):
            prev[i] = prev[values[0]]
        
        for r in range(1, N):
            for c in range(W+1):
                # take
                notTake = prev[c]
                take = 0
                if weights[r] <= c:
                    take = values[r] + prev[c]

                prev[c] = max(take, notTake)
            
        return prev[-1]
    return spacy()

print(rknapsack(N, W, values, weights))
print(mknapsack(N, W, values, weights))
print(tknapsack(N, W, values, weights))
print(sknapsack(N, W, values, weights))
