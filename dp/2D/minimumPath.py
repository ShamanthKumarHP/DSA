class Solution:
    # def minFallingPathSum(self, matrix):
    #     rows = len(matrix) - 1
    #     cols = len(matrix[-1]) - 1
    #     dp = [[-1 for j in range(cols+1)] for i in range(rows+1)]
        
    #     def recursion(row, col, dp):
    #         if col<0 or col > cols:
    #             return int(1e9)
            
    #         if row == 0:
    #             return matrix[row][col]

    #         if dp[row][col] != -1:
    #             return dp[row][col]
            
    #         left_upper = recursion(row-1, col-1, dp) 
    #         right_upper = recursion(row-1, col+1, dp)
    #         upper = recursion(row-1, col, dp)

    #         dp[row][col] = matrix[row][col]  + min([left_upper, right_upper, upper])
            
    #         return dp[row][col]

    #     min_path = int(1e9)
    #     for idx, last in enumerate(matrix[-1]):
    #         mini = recursion(len(matrix)-1, idx, dp)
    #         min_path = min(min_path, mini)

    #     return min_path
    
    # memo
    # def minFallingPathSum(self, matrix):
    #     rows = len(matrix) - 1
    #     cols = len(matrix[-1]) - 1
    #     dp = [[-1 for j in range(cols+1)] for i in range(rows+1)]
        
    #     def tabu():
    #         dp[0] = matrix[0]
    #         for row in range(1, rows+1):
    #             for col in range(cols+1):
                    
    #                 left_upper = int(1e9)
    #                 if col > 0:
    #                     left_upper = dp[row-1][col-1]
                    
    #                 right_upper = int(1e9)
    #                 if col < cols :
    #                     right_upper = dp[row-1][col+1]

    #                 upper = dp[row-1][col]

    #                 dp[row][col] = matrix[row][col]  + min([left_upper, right_upper, upper])
            
    #         # min of last row elements of dp
    #         return min(dp[-1])
    #     return tabu()

    # spacy
    def minFallingPathSum(self, matrix):
        rows = len(matrix) - 1
        cols = len(matrix[-1]) - 1

        def tabu():
            prev_dp = [-1 for j in range(cols+1)]
            prev_dp = matrix[0]
            for row in range(1, rows+1):
                curr_dp = [-1 for j in range(cols+1)]
                for col in range(cols+1):
                    
                    left_upper = int(1e9)
                    if col > 0:
                        left_upper = prev_dp[col-1]
                    
                    right_upper = int(1e9)
                    if col < cols :
                        right_upper = prev_dp[col+1]

                    upper = prev_dp[col]

                    curr_dp[col] = matrix[row][col]  + min([left_upper, right_upper, upper])
                prev_dp = curr_dp[:]
            # min of last row elements of dp
            return min(prev_dp)
        return tabu()