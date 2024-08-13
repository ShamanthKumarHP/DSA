class Solution:
    def numEnclaves(self, grid) -> int:
        # traverse boundaries
        m = len(grid)
        n = len(grid[0])
        stack = []
        visited = [[0 for i in range(n)] for j in range(m)]
        walked_off_lands = 0
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and grid[i][j] == 1:
                    visited[i][j] = 1
                    walked_off_lands = walked_off_lands + 1
                    stack.append((i,j))
        
        # keep count of number of total lands
        # ans = total_lands - walked off lands

        print("walked_off_lands", walked_off_lands)

        # total number of lands:
        total_land = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_land += 1
        print("total_land", total_land)

        dx = [0 ,0, 1, -1]
        dy = [1, -1, 0, 0]
        

        while stack:
            x,y = stack.pop(0)
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx > m-1 or ny < 0 or ny > n-1 or grid[nx][ny] == 0 or visited[nx][ny] == 1:
                    continue
                visited[nx][ny] = 1
                stack.append((nx,ny))
                walked_off_lands = walked_off_lands + 1
        
        print("walked_off_lands after", walked_off_lands)
        
        
        return total_land - walked_off_lands

obj = Solution()
grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(obj.numEnclaves(grid))