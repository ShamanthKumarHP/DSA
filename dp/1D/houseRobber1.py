# https://leetcode.com/problems/house-robber/description/
class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        n = len(nums) - 1

        # recursion
        def recursion(n):
            if n == 0:
                return nums[0]
            elif n < 0:
                return 0
            
            pick = nums[n] + recursion(n-2)
            notpick = 0 + recursion(n-1)
            
            return max(pick, notpick)
        
        # return recursion(n)


        # memo
        dp = [-1] * (n+1)
        def memo(n, dp):
            if n == 0:
                return nums[0]
            elif n < 0:
                return 0
            
            if dp[n] != -1:
                return dp[n]
            
            pick = nums[n] + memo(n-2, dp)
            notpick = 0 + memo(n-1, dp)
            dp[n] = max(pick, notpick)
            return dp[n]
        
        # return memo(n, dp)


        # tabu

        # dp = [-1] * (n+1)
        # dp[0] = nums[0]
        # for i in range(1, n+1):
        #     # pick = dp[i] + dp[i-2]

        #     pick = nums[i] 
        #     if i > 1:
        #         pick += dp[i-2] 

        #     notpick = 0 + dp[i-1]
        #     dp[i] = max(pick, notpick)
        # return dp[n]
    

        # spacy
        prev1 = nums[0]
        prev2 = 0
        for i in range(1,n+1):
            pick = nums[i]
            if i > 1: 
                pick += prev2
            
            notpick = 0 + prev1

            prev2 = prev1
            prev1 = max(pick, notpick)

        return prev1





    

    
object = Solution()
nums = [2,7,9,3,1]
print(object.rob(nums))


        