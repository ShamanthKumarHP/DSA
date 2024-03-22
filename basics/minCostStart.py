class Solution:
    def minCostArray(self, arr, idx):
        if idx >=len(arr):
            return 0
        return arr[idx] + min(self.minCostArray(arr,idx+1),self.minCostArray(arr,idx+2))
         
    def minCostClimbingStairs(self, cost):
        return min(self.minCostArray(cost,0) , self.minCostArray(cost, 1))

obj1 = Solution()
cost = [10,15,20]
s = obj1.minCostClimbingStairs(cost)
print(s)