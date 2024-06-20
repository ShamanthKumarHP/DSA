class Solution:
    def minCost(self, n: int, cuts) -> int:
        dp = [[-1 for i in range(n+1)] for i in range(n+1)]
        def recursion(i,j):
            # partition dp bc
            if i > j:
                # during edge cuttings
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            
            mini = int(1e9)
            for k in range(i, j+1):
                cost = cuts[j+1] - cuts[i-1] # current total length (has last cut info)
                cost = cost + recursion(i,k-1) + recursion(k+1, j)
                mini = min(mini, cost)
                dp[i][j] = mini
            return mini
        

        # first sort
        cuts.sort()
        cuts.insert(0,0)  # left start 
        cuts.append(n) # right end
        return recursion(1, len(cuts)-2)
    
ob = Solution()
print(ob.minCost(3,[1,2]))
        