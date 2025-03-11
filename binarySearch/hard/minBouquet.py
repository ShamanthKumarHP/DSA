class Solution:
    def checkAdjacent(self, bloomDay, mid, adjacent):
        cnt = 0
        bouquet_nums = 0
        for i in bloomDay:
            if i <= mid:
                cnt = cnt + 1
            else:
                cnt = 0
            if cnt == adjacent:
                cnt = 0
                bouquet_nums += 1

        return bouquet_nums

    
    def minDays(self, bloomDay, m, k):
        if m*k > len(bloomDay):
            return -1
        high = max(bloomDay)
        low = 1
        ans = -1
        while low <= high:
            mid = int((low+high)/2)
            bouquet_nums = self.checkAdjacent(bloomDay, mid, k)
            print(f"{mid} , {bouquet_nums}")
            if bouquet_nums >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
            

obj = Solution()
bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
print(obj.minDays(bloomDay, m , k))

        