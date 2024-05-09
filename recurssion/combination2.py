# https://leetcode.com/problems/combination-sum-ii/description/

# NOTE for loop patterns
class Solution:
    def combination_recurssion(self, ans, data, i, candidates, target):
        # base condition order matters
        if target == 0:
            # store as value
            ans.append(data[:])
            return
        if target < 0:
            return
        if i == len(candidates):
            return
        for idx in range(i, len(candidates)):
            if idx > i and candidates[idx] == candidates[idx-1]:
                continue

            data.append(candidates[idx])
            target = target - candidates[idx]
            self.combination_recurssion(ans, data, idx+1, candidates, target)
            data.pop()
            target = target + candidates[idx]
        
        return ans

    def combinationSum(self, candidates, target):
        data = []
        ans = []
        candidates.sort()
        return self.combination_recurssion(ans, data, 0, candidates, target)
    
candidates = [10,1,2,7,6,1,5]
target = 8
object = Solution()
print(object.combinationSum(candidates, target))


# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

l = []
l.delete(1)