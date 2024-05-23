class Solution:
    def uniquePaths(self, m, n):
        # def recursion_travel(row, col, m, n):
        #     cnt = 0
            
        #     if row == m and col == n:
        #         return 1
            
        #     if row > m or col > n:
        #         return 0
        
        #     #right
        #     cnt = cnt + recursion_travel(row, col+1, m, n)
        #     #down
        #     cnt = cnt + recursion_travel(row+1, col, m, n)
        
        #     return cnt
        
        # return recursion_travel(0,0,m-1,n-1)

        # def memo(row, col, dp):
        #     if row == m-1 and col == n-1:
        #         return 1
        #     if row > m-1 or col > n-1:
        #         return 0
        #     if dp[row][col] != -1:
        #         return dp[row][col]
            
        #     dp[row][col] = memo(row, col+1, dp) + memo(row+1, col, dp)

        #     return dp[row][col]
        # row = 0
        # col = 0
        # dp = [[-1 for j in range(n) ] for i in range(m)]
        # return memo(row, col, dp)
    
        # tabu
        # better was to start recurssion from top to bottom. anyways


        # def tabu():
        #     dp = [[-1 for j in range(n) ] for i in range(m)]
        #     for i in range(m-1,-1,-1):
        #         right = 0
        #         for j in range(n-1,-1,-1):
        #             if obstacleGrid[i][j] == 1:
        #                 dp[i][j] = 0
        #             elif i == m-1 and j == n-1:
        #                 dp[i][j] = 1
        #             else:
        #                 right = 0
        #                 down = 0
        #                 if j+1 < n:
        #                     right = dp[i][j+1]
        #                 if i + 1 < m:
        #                     down = dp[i+1][j]
                        
        #                 dp[i][j] = right+down

        #     return dp[0][0]
        # return tabu()

        def spacy(m,n):            
            down_array = [0] * n
            for i in range(m-1,-1,-1):
                prev_right = 0
                for j in range(n-1,-1,-1):
                    if i == m-1 and j == n-1:
                        prev_right = 1
                    else:
                        right = 0
                        down = 0
                        if j+1 < n:
                            right = prev_right
                        if i + 1 < m:
                            down = down_array[j]
                        
                        prev_right = right+down
                    down_array[j] = prev_right
                
            return down_array[0]


        dp = [[-1 for j in range(n) ] for i in range(m)]
        return spacy( dp)
        



        
        