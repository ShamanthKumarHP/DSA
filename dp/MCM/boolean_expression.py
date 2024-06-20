def recursion_boolean(arr):  
    dp = [[[ -1 for tf in range(2)] for j in range(len(arr))] for i in range(len(arr))] 
    def recursion(i, j, wantTrue):
        if i > j : 
            return 0
        
        # can be made simple,
        if i == j:
            if wantTrue == 1:
                if arr[i] == "T":
                    return 1
                else:
                    return 0
            else:
                if arr[i] == "F":
                    return 1
                else:
                    return 0
        
        if dp[i][j][wantTrue] != -1:
            return dp[i][j][wantTrue]

        ways = 0
        # have to partition on symbols
        for k in range(i+1, j, 2):
            # just calculate all possbility
            lt = recursion(i, k-1, 1)
            lf = recursion(i, k-1, 0)
            rt = recursion(k+1, j, 1)
            rf = recursion(k+1, j, 0)

            if arr[k] == '&':
                if wantTrue:
                    ways = ways + (lt*rt)
                else:
                    ways = ways + (lf*rf) + (lf*rt) + (lt*rf)
            
            elif arr[k] == '^':
                if wantTrue:
                    ways = ways + (lf*rt) + (lt*rf)
                else:
                    ways = ways + (lf*rf) + (lt*rt)
            
            elif arr[k] == '|':
                if wantTrue:
                    ways = ways + (lt*rt) + (lf*rt) + (lt*rf)
                else:
                    ways = ways + (lf*rf)

        dp[i][j][wantTrue] = ways
        return dp[i][j][wantTrue]
    return recursion(0, len(arr)-1, wantTrue=1)


def tabu_boolean(arr):
    n = len(arr)
    dp = [[[ 0 for tf in range(2)] for j in range(len(arr))] for i in range(len(arr))] 

    for i in range(n-1, -1, -1):
        for j in range(i, n):
            for wantTrue in range(2):
                if i == j:
                    if wantTrue:
                        if arr[i] == 'T':
                            dp[i][j][wantTrue] = 1
                        else:
                            dp[i][j][wantTrue] = 0
                    else:
                        if arr[i] == 'F':
                            dp[i][j][wantTrue] = 1
                        else:
                            dp[i][j][wantTrue] = 0
                    continue

                ways = 0
                # have to partition on symbols
                for k in range(i+1, j, 2):
                    # just calculate all possbility
                    lt = dp[i][k-1][1]
                    lf = dp[i][k-1][0]
                    rt = dp[k+1][j][1]
                    rf = dp[k+1][j][0]

                    if arr[k] == '&':
                        if wantTrue:
                            ways = ways + (lt*rt)
                        else:
                            ways = ways + (lf*rf) + (lf*rt) + (lt*rf)
                    
                    elif arr[k] == '^':
                        if wantTrue:
                            ways = ways + (lf*rt) + (lt*rf)
                        else:
                            ways = ways + (lf*rf) + (lt*rt)
                    
                    elif arr[k] == '|':
                        if wantTrue:
                            ways = ways + (lt*rt) + (lf*rt) + (lt*rf)
                        else:
                            ways = ways + (lf*rf)
                dp[i][j][wantTrue] = ways
    print(dp)
    return dp[0][n-1][1]

exp = "F|T^F"

print(recursion_boolean(exp))
print(tabu_boolean(exp))
