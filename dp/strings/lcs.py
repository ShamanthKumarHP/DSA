class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # def recursion(idx1, idx2):
        #     if idx1 < 0 or idx2 < 0:
        #         return 0
            
        #     if text1[idx1] == text2[idx2]:
        #         return 1 + recursion(idx1-1, idx2-1)
        #     else:
        #         take1 = recursion(idx1, idx2-1)
        #         take2 = recursion(idx1-1, idx2)
        #         return max(take1, take2)
        # return recursion(len(text1)-1, len(text2)-1)

        # dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        # def memo(idx1, idx2):
        #     if idx1 < 0 or idx2 < 0:
        #         return 0

        #     if dp[idx1][idx2] != -1:
        #         return dp[idx1][idx2]

        #     if text1[idx1] == text2[idx2]:
        #         dp[idx1][idx2] = 1 + memo(idx1-1, idx2-1)
        #         return dp[idx1][idx2]
        #     else:
        #         take1 = memo(idx1, idx2-1)
        #         take2 = memo(idx1-1, idx2)
        #         dp[idx1][idx2] = max(take1, take2)
        #         return dp[idx1][idx2]
        # return memo(len(text1)-1, len(text2)-1)
            
        # dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        # def memo(idx1, idx2):
        #     if idx1 < 0 or idx2 < 0:
        #         return 0

        #     if dp[idx1][idx2] != -1:
        #         return dp[idx1][idx2]

        #     if text1[idx1] == text2[idx2]:
        #         dp[idx1][idx2] = 1 + memo(idx1-1, idx2-1)
        #         return dp[idx1][idx2]
        #     else:
        #         take1 = memo(idx1, idx2-1)
        #         take2 = memo(idx1-1, idx2)
        #         dp[idx1][idx2] = max(take1, take2)
        #         return dp[idx1][idx2]
        # return memo(len(text1)-1, len(text2)-1)
            
        
        # def tabu():
        #     dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        #     for idx1 in range(1, len(text1)+1):
        #         for idx2 in range(1, len(text2)+1):
        #             if text1[idx1-1] == text2[idx2-1]:
        #                 dp[idx1][idx2] = 1 + dp[idx1-1][idx2-1]
        #             else:
        #                 take1 = dp[idx1][idx2-1]
        #                 take2 = dp[idx1-1][idx2]
        #                 dp[idx1][idx2] = max(take1, take2) 
        #     return dp[-1][-1]
        # return tabu()  

        def spacy():
            prev = [0 for _ in range(len(text2)+1)]
            curr = [0 for _ in range(len(text2)+1)]
            for idx1 in range(1, len(text1)+1):
                for idx2 in range(1, len(text2)+1):
                    if text1[idx1-1] == text2[idx2-1]:
                        curr[idx2] = 1 + prev[idx2-1]
                    else:
                        take1 = curr[idx2-1]
                        take2 = prev[idx2]
                        curr[idx2] = max(take1, take2) 
                prev = curr[:]
            return prev[-1]
        return spacy()  
        
        