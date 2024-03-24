# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(prices) -> int:
    buy = prices[0]
    highProfit = 0
    for i in range(1, len(prices)):
        profit = prices[i] - buy
        highProfit = max(highProfit, profit)
        buy = min(buy, prices[i])
    return highProfit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))