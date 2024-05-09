# NOTE pick and non pick pattern
class Solution:
    def combination_recurssion(self, ans, data, i, candidates, target):
        # base condition
        if target == 0:
            ans.append(list(data))
            return
        
        if i == len(candidates):
            return
        if target < 0:
            return
            
        data.append(candidates[i])
        target = target - candidates[i]
        self.combination_recurssion(ans, data, i, candidates, target)
        data.remove(candidates[i])
        target = target + candidates[i]
        self.combination_recurssion(ans, data, i+1, candidates, target)
        return ans

    def combinationSum(self, candidates, target):
        data = []
        ans = []
        return self.combination_recurssion(ans, data, 0, candidates, target)
    
candidates = [2,3,6,7] 
target = 7
object = Solution()
print(object.combinationSum(candidates, target))


# Note
a = ['1']
l = list()
l.append(list(a))
a[0] = '2'
print(l)



# TC : 2**t * K
# where t is target value
# K -> ans.append(list(data))
# 2**t -> if [1] and target is 10 -> pick and not pick -> 2 -> 2 ** t