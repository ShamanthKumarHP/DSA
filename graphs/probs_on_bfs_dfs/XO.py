class Solution:

    def solve_bfs(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # use not gate operation
        # 0's which are connected to boundary, keep it 0
        # all others make it as X
        # keep track of visited 
        
        m = len(board)
        n = len(board[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        
        stack = []
        for i in range(m):
            for j in range(n):
                # travel boundaries
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == "O":
                    stack.append((i,j))
                    visited[i][j] = 1
        
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        while stack:
            x,y = stack.pop(0)
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny] == 1 or board[nx][ny] != "O":
                    continue
                visited[nx][ny] = 1
                stack.append((nx,ny))
        
        # ans = [["X" for i in range(m)] for j in range(n)]

        for i in range(m):
            for j in range(n):
                if visited[i][j] == 1:
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        return

    def dfs(self, board, visited, x, y, m, n):
        if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] == 1 or board[x][y] != "O":
            return
        
        visited[x][y] = 1
        
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            self.dfs(board, visited, nx, ny, m, n)
        return

    def solve_dfs(self, board):
        m = len(board)
        n = len(board[0])

        visited = [[0 for i in range(n)] for j in range(m)]

        # get all boundary 0's
        for i in range(m):
            for j in range(n):
                # travel boundaries
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == "O":
                    self.dfs(board, visited, i, j, m, n)

        # for i in [0,m-1]:
        #     for j in range(n):
        #         if board[i][j] == "O":
        #             self.dfs(board, visited, i , j , m , n)
        
        # for i in [0, n-1]:
        #     for j in range(m):
        #         if board[i][j] == "O":
        #             self.dfs(board, visited, i , j, m, n)
        
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 1:
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

obj = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
dfs_board = board.copy()

obj.solve_bfs(board)
print(board)

obj.solve_dfs(dfs_board)
print(dfs_board)