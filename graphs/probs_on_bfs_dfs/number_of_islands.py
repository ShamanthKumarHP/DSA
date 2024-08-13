class Solution:
    def get_islands(self, grid, visited, x, y, m, n):
        
        stack = []
        stack.append((x,y))
        dx = [0,0,1,-1,-1,1,1,-1]
        dy = [1,-1,0,0,1,-1,1,-1]
        
        visited[x][y] = 1
        while stack:
            (mx, my) = stack.pop()
            for k in range(8):
                nx = mx + dx[k]
                ny = my + dy[k]
                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny] == 1 or grid[nx][ny] == 0:
                    continue
                visited[nx][ny] = 1
                stack.append((nx,ny))
        return

    def islands(self, grid):
        # using bfs
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        lands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    lands = lands + 1
                    self.get_islands(grid,visited, i, j , m, n)

        return lands


obj = Solution()
grid = [[1,1,0],[0,1,0],[0,0,0],[0,1,0]]
print(obj.islands(grid))