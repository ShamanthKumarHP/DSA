class Solution:
    def orangesRotting(self, grid) -> int:
        if not grid:
            return -1
        # get all rotten oranges
        rows = len(grid)
        cols = len(grid[0])
        rottenGrid = [[0 for i in range(rows)] for j in range(cols)]
        stack = []
        tot_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    stack.append((r,c))
                    rottenGrid[r][c] = 2
                
                elif grid[r][c] != 0:
                    tot_count += 1
    
        total_rotten = 0
        time = 0
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        while stack:
            size = len(stack)
            while size:
                (cr, cc) = stack.pop(0)
                for i in range(4):
                    nx = cr + dx[i]
                    ny = cc + dy[i]
                    if nx >= 0 and nx < rows and ny >= 0 and ny < cols \
                        and grid[nx][ny] == 1 and rottenGrid[nx][ny] == 0:
                        total_rotten += 1
                        rottenGrid[nx][ny] = 2
                        stack.append((nx,ny))
                size = size - 1
            if stack:
                time = time + 1
                
        if tot_count == total_rotten:
            return time
        else:
            return -1

ob = Solution()
grid = [[1,2]]
print(ob.orangesRotting(grid))