class Solution:
    def change(self, amount, coins):
        def recursion(idx, target):
            if idx == 0:
                if (target % coins[0] == 0):
                    # means target can be achieved
                    # one possible way, that has to consider (target // coins[0]) coins
                    return 1
                else:
                    return 0

            notTake = 0 + recursion(idx - 1, target)
            take = 0
            if target >= coins[idx]:
                take = recursion(idx, target - coins[idx])

            return take + notTake
        # ans = recursion(len(coins)-1, amount)
        # return ans


        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        def memo(idx, target):
            if idx == 0:
                if target % coins[0] == 0:
                    return 1
                else:
                    return 0
            
            if dp[idx][target] != -1:
                return dp[idx][target]
        
            notTake = memo(idx-1, target)
            take = 0
            if target >= coins[idx]:
                take = memo(idx, target-coins[idx])

            return take + notTake
        #return memo(len(coins)-1, amount)

        def tabu():
            dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
            
            for tar in range(amount+1):
                if amount % coins[0] ==0:
                    dp[0][tar] = 1
            
            for idx in range(1, len(coins)):
                for target in range(0, amount+1):
                    # not take
                    notTake = dp[idx-1][target]

                    take = 0
                    if target >= coins[idx]:
                        take = dp[idx][target - coins[idx]]
                    
                    dp[idx][target] = take + notTake
            
            return dp[-1][-1]
        #return tabu()
    
        def spacy():
            prev = [0 for _ in range(amount+1)]
            curr = [0 for _ in range(amount+1)]

            for tar in range(amount+1):
                if amount % coins[0] ==0:
                    prev[tar] = 1

            for idx in range(1, len(coins)):
                for target in range(0, amount+1):
                    # not take
                    notTake = prev[target]

                    take = 0
                    if target >= coins[idx]:
                        take = curr[target - coins[idx]]
                    
                    curr[target] = take + notTake
                prev = curr
            return prev[-1]




    
a = Solution()
print(a.change(5, [1,2,5]))
            
        