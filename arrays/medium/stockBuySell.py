# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit1(self, prices) -> int:
        buy = prices[0]
        highProfit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - buy
            highProfit = max(highProfit, profit)
            buy = min(buy, prices[i])
        return highProfit
    
    def maxProfit2(self, prices):
        def space():
            prev = [0 for j in range(2)]
            curr = prev[:]
            n = len(prices)
            for idx in range(n-1, -1, -1):
                for buy in range(0,2):
                    # buy
                    if buy  == 1:
                        # take
                        take = - prices[idx] + prev[0]
                        # not take
                        notTake = 0 + prev[1] 
                        curr[buy] = max(take, notTake)
                    else:
                        #sell
                        take = prices[idx] + prev[1]
                        # notSell
                        notTake = 0 + prev[0]
                        curr[buy] = max(take, notTake)
                prev = curr[:]  
            return prev[1]
        return space()

    def maxProfit4(self, k: int, prices) -> int:
        def space():
            n = len(prices)
            prev = [[0 for i in range(k+1)] for j in range(2)]
            curr = [[0 for i in range(k+1)] for j in range(2)]

            for idx in range(n-1, -1, -1):
                for buy in range(0,2):
                    for count in range(1,k+1):
                        if buy:
                            take = -prices[idx] + prev[0][count]
                            notTake = 0 + prev[buy][count]
                            curr[buy][count] = max(take, notTake)
                        else:
                            sell = prices[idx] + prev[1][count-1]
                            notSell = 0 + prev[0][count]
                            curr[buy][count] = max(sell, notSell)
                prev = curr[:]
            return prev[1][k]
        return space()

obj = Solution()

prices = [3,2,6,5,0,3]
print("maxProfit1", obj.maxProfit1(prices))
print("maxProfit2", obj.maxProfit2(prices))
# print(obj.maxProfit4(2, [3,2,6,5,0,3]))
                            







        