 # refer leetcode
class Solution:
    def maxProfit(self, prices) -> int:
        # greedy
        # sum = 0
        # for i in range(1, len(prices)):
        #     if prices[i] >= prices[i-1]:
        #         sum += (prices[i] - prices[i-1])
        # return sum

        # def recursion(idx, buy):
        #     if idx == len(prices):
        #         return 0
            
        #     if buy:
        #         # take
        #         take = - prices[idx] + recursion(idx+1, buy=0)
        #         # not take
        #         notTake = 0 + recursion(idx+1, buy=1)
        #         return max(take, notTake)
        #     else:
        #         #sell
        #         take = prices[idx] + recursion(idx+1, buy=1)
        #         # notSell
        #         notTake = 0 + recursion(idx+1, buy=0)
        #         return max(take, notTake)
        # return recursion(0, buy=True)

        # dp = [[ -1 for j in range(2)] for i in range(len(prices))]
        # def memo(idx, buy):
        #     if idx == len(prices):
        #         return 0

        #     if dp[idx][buy] != -1:
        #         return dp[idx][buy]

        #     if buy:
        #         # take
        #         take = - prices[idx] + memo(idx+1, buy=0)
        #         # not take
        #         notTake = 0 + memo(idx+1, buy=1)
        #         dp[idx][buy] = max(take, notTake)
        #         return dp[idx][buy]
        #     else:
        #         #sell
        #         take = prices[idx] + memo(idx+1, buy=1)
        #         # notSell
        #         notTake = 0 + memo(idx+1, buy=0)
        #         dp[idx][buy] = max(take, notTake)
        #         return dp[idx][buy]
        # return memo(0, buy=1)

        # refer leetcode
        return
        