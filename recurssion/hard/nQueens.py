class Solution:
    # def isSafe(self, row_idx, col_idx, board):
    #     # left sides 3 directions check is enough
    #     n = len(board)
    #     row = row_idx
    #     col = col_idx
    #     # check left
    #     while col >=0:
    #         if board[row][col] == "Q":
    #             return False
    #         col -= 1
        
    #     row = row_idx
    #     col = col_idx
    #     # check left upper diagonal
    #     while row >= 0 and col >= 0:
    #         if board[row][col] == "Q":
    #             return False
    #         row -= 1
    #         col -= 1

    #     row = row_idx
    #     col = col_idx
    #     # check left lower diagonal
    #     while row < n and col >= 0:
    #         if board[row][col] == "Q":
    #             return False
    #         row += 1
    #         col -= 1

    #     return True

    # def backtrack(self, col, board, ans):
    #     if col == len(board):
    #         copy = [''.join(row) for row in board]
    #         ans.append(copy)
    #         return
            
    #     for row in range(len(board)):
    #         if (self.isSafe(row, col, board)):
    #             board[row][col] = "Q"
    #             self.backtrack(col+1, board, ans)
    #             board[row][col] = "." 
    #     return ans
    
    # def solveNQueens(self, n):
    #     board = []
    #     for i in range(n):
    #         temp = ["."] * n
    #         board.append(temp)
    #     return self.backtrack(0, board, [])


    # Optimal
    
    def backtrackOptimal(self, col, board, ans, lowerDiagonal, upperDiagonal, leftRow):
        if col == len(board):
            copy = [''.join(row) for row in board]
            ans.append(copy)
            return
         
        for row in range(len(board)):
            if not leftRow.get(row, False) \
            and not lowerDiagonal.get(row+col, False) \
            and not upperDiagonal.get( len(board)-1 + (col - row), False):
                
                board[row][col] = "Q"

                leftRow[row] = True
                upperDiagonal[len(board)-1 + (col - row)] = True
                lowerDiagonal[row+col] = True

                self.backtrackOptimal(col+1, board, ans, lowerDiagonal, upperDiagonal, leftRow)
                board[row][col] = "."
                
                leftRow[row] = False
                upperDiagonal[len(board)-1 + (col - row)] = False
                lowerDiagonal[row+col] = False
        return ans
    
    def solveNQueensOptimal(self, n):
        board = []
        for i in range(n):
            temp = ["."] * n
            board.append(temp)
        return self.backtrackOptimal(0, board, [], {}, {}, {})
        





object = Solution()
# print(object.solveNQueens(4))
# isSafe function takes additional of 3N time
print()
print(object.solveNQueensOptimal(4))


        
        