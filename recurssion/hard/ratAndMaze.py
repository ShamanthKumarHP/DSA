# lexico = "DLRU"
maze = [[1, 0, 0, 0],
        [1, 1, 0, 1], 
        [1, 1, 0, 0], 
        [0, 1, 1, 1]]

def backtrack(maze, row, col, ans, ds, direction):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
            ans.append(ds[:])
            return
    if row == len(maze) or row < 0 or col == len(maze[0]) or col < 0:
        return 
    if maze[row][col] == 0:
        return
    if maze[row][col] == "visited":
        return
    if maze[row][col] == 1:
        maze[row][col] = "visited"
        ds.append(direction)
        
        #down
        backtrack(maze, row+1, col, ans, ds,"D")
        #left
        backtrack(maze, row, col-1, ans, ds,"L")
        #right
        backtrack(maze, row, col+1, ans, ds,"R")
        #up
        backtrack(maze, row-1, col, ans, ds,"U")
    
        maze[row][col] = 1
        ds.pop()
    return ans
print(backtrack(maze, 0, 0, [], [], "D"))

