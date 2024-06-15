class Solution:
    def lengthOfLIS(self, nums) -> int:
        # def recursion(idx, prev):
        #     if idx == len(nums):
        #         return 0

        #     # take 
        #     take = 0
        #     notTake = 0
        #     if prev == -1 or nums[idx] > nums[prev]:
        #         take =  1 + recursion(idx+1, prev=idx)
            
        #     notTake = 0 + recursion(idx+1, prev)
        #     return max(take, notTake)
                
        # return recursion(0, prev=-1)

       
        
        def tab():
            n = len(nums)
            dp = [[0 for i in range(n+1)] for i in range(n+1)]

            # base case
            for i in range(n+1):
                dp[n][i] = 0
            
            for idx in range(n-1, -1, -1):
                for prev in range(idx, -2, -1):
                    # take 
                    take = 0
                    notTake = 0
                    if prev == -1 or nums[idx] > nums[prev]:
                        take =  1 + dp[idx+1][idx+1]
                    notTake = 0 + dp[idx+1][prev+1]

                    dp[idx][prev+1] = max(take, notTake)
            print(dp)
            return dp[0][0]
        return tab()
    
        # best solution
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    take = dp[j] + 1
                    notTake = dp[i] 
                    dp[i] =  max(take, notTake)
        return max(dp)
        
       

    
        

ob = Solution()
nums = [10,15,30,9,40]
print(ob.lengthOfLIS(nums))

        