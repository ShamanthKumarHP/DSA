class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        if grid[0][0] != 0 or grid[-1][-1]!=0:
            return -1
        
        dx = [0 , 0,1,-1,1, 1,-1,-1]
        dy = [1,-1, 0, 0,1,-1,-1,1]

        r = len(grid)
        c = len(grid[0])

        q = []
        q.append((1,0,0)) # val, x, y
        
        visited = [[0 for i in range(c)] for j in range(r)]
        visited[0][0] = 1
        while q:
            cnt, x, y = q.pop(0)

            if x == r-1 and y == c-1:
                return cnt
            
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx >= r or ny < 0 or ny >= c or grid[nx][ny] !=0 or visited[nx][ny] != 0:
                    continue
                visited[nx][ny] = 1
                q.append((cnt+1, nx,ny))
        return -1

obj = Solution()
grid = [[0,0]]
print(obj.shortestPathBinaryMatrix(grid))