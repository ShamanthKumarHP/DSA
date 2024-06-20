class Solution:
    def countSquares(self, matrix) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        total = 0
        dp = [ [0] * cols] * rows
        dp2 =  [[0 for j in range(cols)] for i in range(rows)]
        # fill firsst row and col as same as matrix
        
        for i in range(rows):
            dp[i][0] = matrix[i][0]
            dp2[i][0] = matrix[i][0]
            # total = total + dp[i][0]

        for i in range(cols):
            dp[0][i] = matrix[0][i]
            # total = total + dp[0][i]

        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i][j-1], min(dp[i-1][j-1], dp[i-1][j])) + 1
                else:
                    dp[i][j] = 0

                # total = total + dp[i][j]
        
        for i in dp:
            total = total + sum(i)

        return total
        
a = Solution()
matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
print(a.countSquares(matrix))