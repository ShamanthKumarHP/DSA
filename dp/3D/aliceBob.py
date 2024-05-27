def maximumChocolates(r: int, c: int, grid) -> int:
    # write your code here
    # rows = r-1
    # cols = c-1
    # def recursion(row, j1, j2):
    #     # row movement is same for alice and bob
    #     if j1 < 0 or j2 < 0 or j1 > cols or j2 > cols:
    #         return 0

    #     if row == rows:
    #         if j1 == j2:
    #             # add once
    #             return grid[row][j1]
    #         else:
    #             return grid[row][j1] + grid[row][j2]
        
    #     # for one movement of alice, there could be 3 movements for bob
    #     # so alice can move 3 directions, so there is 9 possibilities.
    #     # we have to check if we both of are in same col
    #     # if same column, add once and explore all the paths
    #     # else add separately and explore all the paths
    #     maxi = int(-1e9)
    #     for dj1 in range(-1, 2, 1):
    #         for dj2 in range(-1, 2, 1):
    #             if j1==j2:
    #                 maxi = max(maxi, grid[row][j1] + recursion(row+1, j1+dj1, j2+dj2))
    #             else:
    #                 maxi = max(maxi, (grid[row][j1] + grid[row][j2] + recursion(row+1, j1+dj1, j2+dj2)))
                
    #     return maxi
    # return recursion(0,0,cols)


    # rows = r-1
    # cols = c-1
    # dp = [[[-1 for j2 in range(cols+1)] for j1 in range(cols+1)] for i in range(rows+1)]

    # def memo(row, j1, j2):
    #     # row movement is same for alice and bob
    #     if j1 < 0 or j2 < 0 or j1 > cols or j2 > cols:
    #         return 0

    #     if dp[row][j1][j2] != -1:
    #         return dp[row][j1][j2]
        
    #     if row == rows:
    #         if j1 == j2:
    #             # add once
    #             return grid[row][j1]
    #         else:
    #             return grid[row][j1] + grid[row][j2]
        
    #     # for one movement of alice, there could be 3 movements for bob
    #     # so alice can move 3 directions, so there is 9 possibilities.
    #     # we have to check if we both of are in same col
    #     # if same column, add once and explore all the paths
    #     # else add separately and explore all the paths
    #     maxi = int(-1e9)
    #     for dj1 in range(-1, 2, 1):
    #         for dj2 in range(-1, 2, 1):
    #             if j1==j2:
    #                 maxi = max(maxi, grid[row][j1] + memo(row+1, j1+dj1, j2+dj2))
    #             else:
    #                 maxi = max(maxi, (grid[row][j1] + grid[row][j2] + memo(row+1, j1+dj1, j2+dj2)))
        
    #     dp[row][j1][j2] = maxi
    #     return dp[row][j1][j2]
    # return memo(0,0,cols)


    # tabulation
    # rows = r-1
    # cols = c-1
    # dp = [[[-1 for j2 in range(cols+1)] for j1 in range(cols+1)] for i in range(rows+1)]

    # # for base case ie last row
    # for j1 in range(0, cols+1):
    #     for j2 in range(0, cols+1):
    #         if j1 == j2:
    #             dp[rows][j1][j2] = grid[rows][j1]
    #         else:
    #             dp[rows][j1][j2] = grid[rows][j1] + grid[rows][j2]
    
    # # start from last second row
    # for row in range(rows-1, -1, -1):
    #     for j1 in range(0, cols+1):
    #         for j2 in range(0, cols+1):
    #             maxi = int(-1e9)
    #             # to try all combinations
    #             for dj1 in range(-1,2,1):
    #                 for dj2 in range(-1,2,1):
    #                     ans = 0
    #                     if j1 == j2:
    #                         ans = grid[row][j1]
    #                     else:
    #                         ans = grid[row][j1] + grid[row][j2]
                        
    #                     # after adding current boxes, check for other paths to get max

    #                     if (j1+dj1 > cols or j2+dj2 > cols or j1+dj1 < 0 or j2+dj2 < 0):
    #                         ans =  ans + int(-1e9)
    #                     else:
    #                         ans = ans + dp[row+1][j1+dj1][j2+dj2]
    #                     maxi = max(maxi, ans)
    #             dp[row][j1][j2] = maxi
    # return dp[0][0][cols]


    rows = r-1
    cols = c-1
    prev_dp = [[-1 for j2 in range(cols+1)] for j1 in range(cols+1)]
    
    # for base case ie last row
    for j1 in range(0, cols+1):
        for j2 in range(0, cols+1):
            if j1 == j2:
                prev_dp[j1][j2] = grid[rows][j1]
            else:
                prev_dp[j1][j2] = grid[rows][j1] + grid[rows][j2]
    
    
    # start from last second row
    for row in range(rows-1, -1, -1):
        curr_dp = [[-1 for j2 in range(cols+1)] for j1 in range(cols+1)]
        for j1 in range(0, cols+1):
            for j2 in range(0, cols+1):
                maxi = int(-1e9)
                # to try all combinations
                for dj1 in range(-1,2,1):
                    for dj2 in range(-1,2,1):
                        ans = 0
                        if j1 == j2:
                            ans = grid[row][j1]
                        else:
                            ans = grid[row][j1] + grid[row][j2]
                        
                        # after adding current boxes, check for other paths to get max

                        if (j1+dj1 > cols or j2+dj2 > cols or j1+dj1 < 0 or j2+dj2 < 0):
                            ans =  ans + int(-1e9)
                        else:
                            ans = ans + prev_dp[j1+dj1][j2+dj2]
                        maxi = max(maxi, ans)
                curr_dp[j1][j2] = maxi
        prev_dp = curr_dp[:]
    return prev_dp[0][cols]


grid = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
r = len(grid)
c = len(grid[0])
print(maximumChocolates(r,c, grid))

