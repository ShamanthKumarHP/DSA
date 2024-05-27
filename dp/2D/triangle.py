# https://leetcode.com/problems/triangle/
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        dp = [[-1 for j in range(len(triangle[-1]))] for i in range(len(triangle))]
        def recursion(row, col):
            # means reached last row
            if row == rows-1:
                return triangle[row][col]
            if dp[row][col] != -1:
                return dp[row][col]
                
            dp[row][col] = triangle[row][col] + \
            min(recursion(row+1,col), recursion(row+1,col+1))

            return dp[row][col]
        row = 0
        col = 0
        return recursion(row,col)
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        dp = [[-1 for j in range(len(triangle[-1]))] for i in range(len(triangle))]
        # copy the last row as it is our base condition
        dp[rows-1] = triangle[rows-1]
        for row in range(rows-2, -1, -1):
            for col in range(row,-1,-1):
                dp[row][col] = triangle[row][col] + \
            min(dp[row+1][col], dp[row+1][col+1])
        return dp[0][0]
        