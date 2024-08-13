class Solution:
    # BFS
    # A particular node will be visited by nearest node for sure.
    def updateMatrix(self, mat):
        stack = []
        m = len(mat)
        n = len(mat[0])
        ans = [[None for i in range(n)] for j in range(m)]

        # first put all ones in stack
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    stack.append((i,j,0))
                    ans[i][j] = 0
        while stack:
            dx = [0,0,-1,1]
            dy = [-1,1,0,0]
            (x,y,d) = stack.pop(0)
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
                if nx < 0 or nx >= m or ny < 0 or ny >= n or ans[nx][ny] != None:
                    continue
                ans[nx][ny] = d + 1
                stack.append((nx,ny,d+1))
        return ans
    

obj = Solution()
mat = [[0,0,0],[0,1,0],[0,0,0]]
print(obj.updateMatrix(mat))