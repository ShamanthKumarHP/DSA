class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        if image[sr][sc] == color:
            # The starting pixel is already colored 0, so no changes are made to the image.
            return image
    
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        stack = []
        stack.append((sr, sc))
        m = len(image)
        n = len(image[0])        
        start_colour = image[sr][sc]
        image[sr][sc] = color
        while stack:
            x,y = stack.pop(0)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < m and ny >= 0 and ny < n and image[nx][ny] == start_colour:
                    stack.append((nx,ny))
                    image[nx][ny] = color
        return image
    
    def floodFillR(self, image, sr: int, sc: int, color: int):
        s = set()
        if image[sr][sc] == color:
            # The starting pixel is already colored 0, so no changes are made to the image.
            return image
        
        def recursion(m, n, start_colour, color, x, y):
            if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != start_colour:
                return
            image[x][y] = color
                # up, right, down, left
            dx = [-1,0,1,0]
            dy = [0,1,0,-1]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                recursion(m, n, start_colour, color, nx, ny)
            return
        m = len(image)
        n = len(image[0])
        start_colour = image[sr][sc]
        recursion( m, n, start_colour, color, sr, sc)
        return image

        
        
ob = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
print(ob.floodFillR(image, 1,1,2))