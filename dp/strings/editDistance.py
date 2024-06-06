class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp = [[-1 for i in range(len(word2))] for j in range(len(word1))]
        # def recursion(i, j):
        #     if i < 0:
        #         return j + 1
        #     if j < 0:
        #         return i + 1
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     if word1[i] == word2[j]:
        #         dp[i][j] = recursion(i-1, j-1)
        #         return dp[i][j]
        #     else:
        #         replace = 1 + recursion(i-1, j-1)
        #         insert = 1 + recursion(i, j-1)
        #         delete = 1 + recursion(i-1, j)
        #         dp[i][j] = min(replace, min(insert, delete)) 
        #         return dp[i][j]
        # return recursion(len(word1)-1, len(word2)-1)
        
        # dp = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]

        # # base case
        # for i in range(len(word1)+1):
        #     dp[i][0] = i
        # for j in range(len(word2)+1):
        #     dp[0][j] = j
        
        # for i in range(1, len(word1)+1):
        #     for j in range(1, len(word2)+1):
        #         if word1[i-1] == word2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             replace = 1 + dp[i-1][j-1]
        #             insert = 1 + dp[i][j-1]
        #             delete = 1 + dp[i-1][j]

        #             dp[i][j] = min(replace, min(insert, delete))
        # return dp[-1][-1]

        # base case
        prev = [i for i in range(len(word2)+1)]
        curr = [0 for i in range(len(word2)+1)]
        
        
        for i in range(1, len(word1)+1):
            curr[0] = i
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    replace = 1 + prev[j-1]
                    insert = 1 + curr[j-1]
                    delete = 1 + prev[j]

                    curr[j] = min(replace, min(insert, delete))
            prev = curr[:]
        return prev[-1]


        
        
a = Solution()
print(a.minDistance("horse", "ros"))