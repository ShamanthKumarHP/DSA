class Solution:
    def RfindTargetSumWays(self, nums, target: int) -> int:
        def recursion(idx, tar):
            if idx == -1:
                if tar == 0:
                    return 1
                else:
                    return 0
            
            notPick = recursion(idx-1, tar)
            pick = 0
            if nums[idx] <= tar:
                pick = recursion(idx-1, tar-nums[idx])

            return notPick + pick
        
        return recursion(len(nums)-1, target)
    
    def MfindTargetSumWays(self, nums, target: int) -> int:
        dp = [[-1 for j in range(target+1)] for i in range(len(nums))] 
        def memo(idx, tar):
            if idx == -1:
                if tar == 0:
                    return 1
                else:
                    return 0

            if dp[idx][tar] != -1:
                return dp[idx][tar]
            
            notPick = memo(idx-1, tar)
            pick = 0
            if nums[idx] <= tar:
                pick = memo(idx-1, tar-nums[idx])

            dp[idx][tar] =  notPick + pick

            return dp[idx][tar] 
        
        return memo(len(nums)-1, target)
    
    def TfindTargetSumWays(self, nums, target: int) -> int:
        dp = [[0 for j in range(target+1)] for i in range(len(nums))] 
        
        # method 1 
        # if i'm at zeroth index and if the value is also 0, and if i have to form sum 0
        # then even if i take or not take sum will be 0
        if nums[0] == 0:
            dp[0][0] = 2
        else:
            if nums[0] <= target:
                dp[0][nums[0]] = 1
        
        for i in range(1, len(nums)):
            for tar in range(0, target+1):
                notPick = dp[i-1][tar]

                pick = 0
                if nums[i] <= tar:
                    pick = dp[i-1][tar-nums[i]]
                
                dp[i][tar] = pick + notPick
        ans = dp[-1][-1]
         
        # Handle if zero is there method 2
        # # check in how many ways we can represent 0
        # # if there are two zeros, then [0], [0], [0,0], []
        # # that is 2 power n

        # # before returning count number of zero is array
        # zero_count = 0
        # for i in nums:
        #     if i == 0:
        #         zero_count += 1
        
        # ans = ans * (2 ** zero_count)
        return ans
    
    def SfindTargetSumWays(self, nums, target: int) -> int:
        prev = [0 for i in range(target+1)]

        if nums[0] == 0:
            prev[0] = 2
        else:
            if nums[0] <= target:
                prev[nums[0]] = 1
        
        for r in range(1, len(nums)):
            curr = [0 for i in range(target+1)]
            for tar in range(0, target+1):
                notPick = prev[tar]

                pick = 0
                if nums[r] <= tar:
                    pick = prev[tar - nums[r]]
                
                curr[tar] = pick + notPick

            prev = curr[:]
    
        ans = prev[-1]
        return ans
             
instance = Solution()
# TODO
nums = [0,0,1]
target = 1

print(instance.RfindTargetSumWays(nums, target))
print(instance.MfindTargetSumWays(nums, target))
print(instance.TfindTargetSumWays(nums, target))
print(instance.SfindTargetSumWays(nums, target))
                

    

    
        