# https://www.geeksforgeeks.org/problems/geeks-training/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=geeks-training


# try to play for base case for index 0

def getMaximum(points):
    days = len(points) - 1
    tasks = len(points[0]) - 1

    def recursion(points, day, tasks, prev_task):
        if day == 0:
            max_sum = float('-inf')
            for task in range(tasks + 1):
                if task != prev_task:
                    max_sum = max(max_sum, points[day][task])
            return max_sum
        
        max_sum = float('-inf')
        for task in range(tasks + 1):
            if task != prev_task:
                get_sum = points[day][task] +  recursion(points, day-1, tasks, current_task=task )
                max_sum = max(max_sum, get_sum)
        
        return max_sum
    
    # return recursion(points, days, tasks, prev_task = -1)

    dp = [[-1 for j in range(4)] for i in range(len(points))]
    def memo(points, day, prev_task, dp):
        if day == 0:
            max_sum = float('-inf')
            for task in range(tasks + 1):
                if task != prev_task:
                    max_sum = max(max_sum, points[day][task])
            dp[day][prev_task] = max_sum
            return dp[day][prev_task]
        
        if dp[day][prev_task] != -1:
            return dp[day][prev_task]
        
        max_sum = float('-inf')
        for task in range(tasks + 1):
            if task != prev_task:
                get_sum = points[day][task] +  memo(points, day-1, task, dp )
                max_sum = max(max_sum, get_sum)

        dp[day][prev_task] = max_sum
        
        return dp[day][prev_task]

    #return memo(points, days, 3, dp)

    def tabu(points, days, dp):
        dp = [[-1 for j in range(4)] for i in range(len(points))]
        dp[0][0] = max(points[0][1], points[0][2])
        dp[0][1] = max(points[0][0], points[0][2])
        dp[0][2] = max(points[0][0], points[0][1])
        dp[0][3] = max(points[0][0], points[0][1], points[0][2])

        for day in range(1, days+1):
            for task in range(4):
                max_sum = float('-inf')
                for t in range(3):
                    if t != task:
                        get_sum = points[day][t] + dp[day-1][t]
                        max_sum = max(get_sum, max_sum)
                        dp[day][task] = max_sum

        return dp[days][3]
    # return tabu(points, days, dp)

    def spacy(points, days, dp):
        dp = [ -1 for i in range(len(points)+1)]
        dp[0] = max(points[0][1], points[0][2])
        dp[1] = max(points[0][0], points[0][2])
        dp[2] = max(points[0][0], points[0][1])
        dp[3] = max(points[0][0], points[0][1], points[0][2])

        for day in range(1, days+1):
            temp = [ -1 for i in range(len(points) + 1) ]
            for task in range(4):
                max_sum = float('-inf')
                for t in range(3):
                    if t != task:
                        get_sum = points[day][t] + dp[t]
                        max_sum = max(get_sum, max_sum)
                        temp[task] = max_sum
            dp = temp[:]

        return dp[3]

    return spacy(points, days, dp)
        
    



points = [[1,2,5],[3,1,1],[3,3,3]]
# points = [[10,40,70],[20,50,80],[30,60,90]]

print(getMaximum(points))