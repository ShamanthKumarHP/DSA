class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # def recursion_travel(row, col, m, n):
        #     cnt = 0
        #     if row > m or col > n:
        #         return 0

        #     if obstacleGrid[row][col] != 0:
        #         return 0
                
        #     if row == m and col == n:
        #         return 1    
        
        #     #right
        #     cnt = cnt + recursion_travel(row, col+1, m, n)
        #     #down
        #     cnt = cnt + recursion_travel(row+1, col, m, n)
        
        #     return cnt
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # return recursion_travel(0,0,m-1,n-1)

        def memo(row, col, dp):
            if row > m-1 or col > n-1:
                return 0
            if obstacleGrid[row][col] != 0:
                return 0
            if row == m-1 and col == n-1:
                return 1
            if dp[row][col] != -1:
                return dp[row][col]
            
            dp[row][col] = memo(row, col+1, dp) + memo(row+1, col, dp)

            return dp[row][col]
        row = 0
        col = 0
        
        dp = [[-1 for j in range(n) ] for i in range(m)]
        return memo(row, col,dp)
        
        