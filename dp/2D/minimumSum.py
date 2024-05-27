# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid):
        # def recursion(row, col):
        #     if col == len(grid[0]) - 1 and row == len(grid) - 1:
        #         return grid[row][col]
            
        #     if col > len(grid[0]) - 1 or row > len(grid) - 1:
        #         return int(1e9)
            
        #     min_sum = grid[row][col] + min(recursion(row+1,col), recursion(row,col+1))
        #     return min_sum

        # return recursion(0,0)

        # def memo(row, col,dp):
        #     if col == len(grid[0]) - 1 and row == len(grid) - 1:
        #         return grid[row][col]
            
        #     if col > len(grid[0]) - 1 or row > len(grid) - 1:
        #         return int(1e9)
            
        #     if dp[row][col] != -1:
        #         return dp[row][col]
            
        #     dp[row][col] = grid[row][col] + min(memo(row+1,col, dp), memo(row,col+1,dp))
        #     return dp[row][col]
        
        # dp = [ [ -1 for j in range(len(grid[0]))] for i in range(len(grid)) ]
        # return memo(0,0,dp)

        # def minPathSum(grid):
        #     rows = len(grid)
        #     cols = len(grid[0])
        #     dp = [[-1 for j in range(cols)] for i in range(rows)]
            
        #     for row in range(rows-1, -1, -1):
        #         for col in range(cols-1, -1, -1):
        #             if row == rows-1 and col == cols-1:
        #                 dp[rows-1][cols-1] = grid[rows-1][cols-1]
        #                 continue
        #             right = float('inf')
        #             down = float('inf')
        #             if col+1 < cols:
        #                 right = dp[row][col+1]
        #             if row+1 < rows:
        #                 down = dp[row+1][col]
        #             dp[row][col] = grid[row][col] + min(right, down)
        #     return dp[0][0]
        # return minPathSum(grid)

        def minPathSum(self, grid) :
            rows = len(grid)
            cols = len(grid[0])
            dp = [-1 for i in range(cols)]
            temp = dp[:]
            for row in range(rows-1, -1, -1):
                for col in range(cols-1, -1, -1):
                    if row == rows-1 and col == cols-1:
                        temp[col] = grid[rows-1][cols-1]
                        continue
                    right = float('inf')
                    down = float('inf')
                    if col+1 < cols:
                        right = temp[col+1]
                    if row+1 < rows:
                        down = dp[col]
                    temp[col] = grid[row][col] + min(right, down)
                dp = temp[:]
            return dp[0]
                    
                    

        

ob = Solution()
grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
print(ob.minPathSum(grid))