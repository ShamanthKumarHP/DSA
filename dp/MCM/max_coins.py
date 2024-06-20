class Solution:
    def maxCoins(self, nums) -> int:
        # last to first ballon burst
        # padding
        nums.insert(0,1)
        nums.append(1)
        dp = [[-1 for i in range(len(nums)+1)] for i in range(len(nums)+1)]
        def recursion(i,j):
            if i > j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            maxi = 0
            for k in range(i, j+1):
                coins = (nums[i-1] * nums[k] * nums[j+1]) \
                        + recursion(i,k-1) + recursion(k+1,j)
                maxi = max(coins, maxi)
            dp[i][j] = maxi
            return maxi
        
        return recursion(1, len(nums)-2)
        