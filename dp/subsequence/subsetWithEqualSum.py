# https://leetcode.com/problems/partition-equal-subset-sum/
class Solution:
    def canPartition(self, nums):
        total = sum(nums)

        # finding half of the total sum, whether we can form subset of that
        # it total is odd, then we cannot have two equal halves
        if total % 2 != 0:
            return False
        
        # be default floor division so.
        target = total // 2
    
        def spacy(target):
            # base case
            # first column ie sum 0, Make as True
            prev = [False for i in range(target+1)]
            prev[0] = True
                
            if nums[0] <= target:
                prev[nums[0]] = True
            
            for i in range(1, len(nums)):
                curr = [False for i in range(target+1)]
                curr[0] = True
                for j in range(1, target+1):
                    # not take
                    notTake = prev[j]

                    # take
                    take = False
                    if nums[i] <= j:
                        remainder = j - nums[i]
                        take = prev[remainder]

                    curr[j] = notTake or take
                prev = curr
            return prev[target]

        return spacy(target)
        