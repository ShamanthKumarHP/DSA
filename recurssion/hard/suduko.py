class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(board, value, row, col):
            for i in range(9):
                # row check
                if board[i][col] == value:
                    return False
                
                # col check
                if board[row][i] == value:
                    return False

                # box check
                if board[ (row//3)*3 + (i//3) ][ (col//3)*3 + (i%3)] == value:
                    return False

            return True

        def backtrack(board):
            for a_row in range(9): 
                for j_col in range(9):
                    if board[a_row][j_col] == ".":
                        for k in "123456789":
                            if (isValid(board, k, a_row, j_col)):
                                board[a_row][j_col] = k
                                if backtrack(board):
                                    return True
                                else:
                                    board[a_row][j_col] = "."
                        
                        return False # since cannot put the 1-9 in last col, start removing
            return True
        
        backtrack(board)
        print(board)

    
object = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
object.solveSudoku(board)


                                    

                   
