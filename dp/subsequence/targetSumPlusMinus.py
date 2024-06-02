class Solution:
    def findTargetSumWays(self, nums, target) -> int:
        # def recursion(idx, tar):
        #     if idx == 0:
        #         if tar - nums[0] == 0:
        #             return 1
        #         elif tar + nums[0] == 0:
        #             return 1
        #         else:
        #             return 0
            
        #     plus =  recursion(idx-1, tar + nums[idx])
        #     minus = recursion(idx-1, tar - nums[idx])
        #     return plus + minus
        
        # return recursion(len(nums)-1, target)

        # recursion better way to avoid negativeity
        # s1 - s2 = target
        # s1 + s2 = total_Sum
        # s1 = (target + totalsum) / 2

        total = sum(nums)
        if (total + target) % 2 !=0:
            return 0
        
        required = (target + total) // 2

        def recursion(idx, req):
            if idx == 0:
                if req == 0 and nums[0] == 0:
                    return 2 # take + notTake
                elif req == 0 or req == nums[0]:
                    return 1 # notTake
                else:
                    return 0 # take
        

            notpick = 0 + recursion(idx-1, req)
            pick = 0
            if nums[idx] <= req:
                pick = recursion(idx-1, req-nums[idx])
            return pick + notpick
        return recursion(len(nums)-1, required)
    
    

    # Function to find the number of ways to partition an array into two subsets
    # with a given target difference using dynamic programming
    def findWays(self, num, tar):
        mod = int(1e9 + 7)
        n = len(num)

        # Initialize a list 'prev' to store results for the previous element
        prev = [0 for i in range(tar + 1)]

        # Initialize 'prev' based on the first element of 'num'
        if num[0] == 0:
            prev[0] = 2  # Two cases - pick and not pick
        else:
            prev[0] = 1  # One case - not pick

        if num[0] != 0 and num[0] <= tar:
            prev[num[0]] = 1  # One case - pick

        for ind in range(1, n):
            # Initialize a list 'cur' to store results for the current element
            cur = [0 for i in range(tar + 1)]
            for target in range(tar + 1):
                notTaken = prev[target]

                taken = 0
                if num[ind] <= target:
                    taken = prev[target - num[ind]]

                # Store the result in 'cur' with modulo operation
                cur[target] = (notTaken + taken) % mod
            prev = cur

        # Return the result for the target sum
        return prev[tar]
    
    def targetSum(self, n, target, arr):
        totSum = 0
        for i in range(n):
            totSum += arr[i]

        # Checking for edge cases
        if (totSum - target) < 0 or ((totSum - target) % 2):
            return 0

        # Calculate and return the number of ways using 'findWays' function
        return self.findWays(arr, (totSum - target) // 2)
    
ob = Solution()
print(ob.targetSum(1, -200, [100]))