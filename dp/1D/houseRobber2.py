# https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        # # remove last element and start
        # prev1 = nums[0]
        # prev2 = 0
        # for i in range(1,n-1):
        #     pick = nums[i]
        #     if i > 1: 
        #         pick += prev2
            
        #     notpick = 0 + prev1

        #     prev2 = prev1
        #     prev1 = max(pick, notpick)
        
        # # remove first element and start
        # new_nums = nums[1:]
        # new_n = len(new_nums)
        # new_prev1 = new_nums[0]
        # new_prev2 = 0
        # for i in range(1,new_n):
        #     pick = new_nums[i]
        #     if i > 1: 
        #         pick += new_prev2
            
        #     notpick = 0 + new_prev1

        #     new_prev2 = new_prev1
        #     new_prev1 = max(pick, notpick)


        # return max(prev1, new_prev1)
        
        def spacy(nums):
            n = len(nums)
            prev1 = nums[0]
            prev2 = 0
            for i in range(1,n):
                pick = nums[i]
                if i > 1: 
                    pick += prev2
                
                notpick = 0 + prev1

                prev2 = prev1
                prev1 = max(pick, notpick)
            return prev1

        return max(spacy(nums[:-1]), spacy(nums[1:]))