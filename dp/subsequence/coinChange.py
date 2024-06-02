class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # def recursion(idx, target):
        #     if idx == 0:
        #         if (target % coins[0] == 0):
        #             return int(target/coins[0])
        #         else:
        #             return int(1e9)
                    
        #     notTake = 0 + recursion(idx - 1, target)
        #     take = int(1e9)
        #     if target >= coins[idx]:
        #         take = 1 + recursion(idx, target - coins[idx])

        #     return min(take, notTake)
        # ans = recursion(len(coins)-1, amount)
        # if ans >= int(1e9):
        #     return -1
        # return ans

        # dp = [[-1 for j in range(amount+1)] for i in range(len(coins))]

        # def memo(idx, target):
        #     if idx == 0:
        #         if (target % coins[0] == 0):
        #             return int(target/coins[0])
        #         else:
        #             return int(1e9)
            
        #     if dp[idx][target] != -1:
        #         return dp[idx][target]

        #     notTake = 0 + memo(idx - 1, target)
        #     take = int(1e9)
        #     if target >= coins[idx]:
        #         take = 1 + memo(idx, target - coins[idx])

        #     dp[idx][target] = min(take, notTake)
            
        #     return dp[idx][target]
        # ans = memo(len(coins)-1, amount)

        # if ans >= int(1e9):
        #     return -1
        # return ans

        # def tabu():
        #     dp = [[0 for j in range(amount+1)] for i in range(len(coins))]

        #     for target in range(amount+1):
        #         if target % coins[0] == 0:
        #             dp[0][target] = target // coins[0]
        #         else:
        #             dp[0][target] = int(1e9)
            
        #     for row in range(1,len(coins)):
        #         for target in range(1, amount+1):
        #             notTake = dp[row-1][target]
        #             take = int(1e9)
        #             if target >= coins[row]:
        #                 take = 1 + dp[row][target-coins[row]]
                    
        #             dp[row][target] = min(take, notTake)
            
        #     if dp[-1][amount] >= int(1e9):
        #         return -1 
        #     return dp[-1][amount]
        # return tabu()

        def spacy():
            prev = [0 for j in range(amount+1)]
            curr = [0 for j in range(amount+1)]

            for target in range(amount+1):
                if target % coins[0] == 0:
                    prev[target] = target // coins[0]
                else:
                    prev[target] = int(1e9)
            
            for row in range(1,len(coins)):
                for target in range(1, amount+1):
                    notTake = prev[target]
                    take = int(1e9)
                    if target >= coins[row]:
                        take = 1 + curr[target-coins[row]]
                    
                    curr[target] = min(take, notTake)

                prev = curr[:]
            if prev[amount] >= int(1e9):
                return -1 
            return prev[amount]
        return spacy()

