class Solution:
    def calculateRequiredDays(self, weights, mid):
        # weights = [1,2,3,4,5,6,7,8,9,10]
        calc_sum = 0
        calc_days = 0
        
        for weight in weights:
            calc_sum = calc_sum + weight
            if calc_sum == mid:
                calc_days += 1
                calc_sum = 0
            elif calc_sum > mid:
                calc_days += 1
                calc_sum = weight
        if calc_sum != 0:
            calc_days +=1
        return calc_days

    def shipWithinDays(self, weights, days):
        high = sum(weights)
        low = max(weights)
        ans = 1
        while low <= high:
            mid = int((low+high)/2)
            calc_days = self.calculateRequiredDays(weights, mid)
            print(mid, calc_days)
            if calc_days > days:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans
weights = [1,2,3,4,5,6,7,8,9,10]
days = 1
obj = Solution()
print(obj.shipWithinDays(weights, days))




        