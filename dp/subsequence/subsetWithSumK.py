def subsetTarget(arr, target):
    def recursion(arr, idx, target):
        if target == 0:
            return True
        if idx == 0:
            # if i reach last index, then I expect my last value is equal to the target
            if target == arr[idx]:
                return True
            else:
                return False
        
        take = False
        if arr[idx] <= target:
            take = recursion(arr, idx-1, target - arr[idx])

        not_take = recursion(arr, idx-1, target)

        return take or not_take
                       
    # return recursion(arr, len(arr)-1, 6)

    dp = [[-1 for j in range(target+1)] for i in range(len(arr))]
    # concept is, previous row mein if remainder is there then yes.
    # previous row will have take and not take concept and it will store remainder value of previous element

    def memo(arr, idx, target):
        if target == 0:
            return True

        if idx == 0:
            # if i reach last index, then I expect my last value is equal to the target
            if target == arr[idx]:
                return True
            else:
                return False

        if dp[idx][target] != -1:
            return dp[idx][target]
        
        take = False
        if arr[idx] <= target:
            take = memo(arr, idx-1, target - arr[idx])

        not_take = memo(arr, idx-1, target)

        dp[idx][target] = take or not_take
        return dp[idx][target]
    # return memo(arr, len(arr)-1, target)


    def tabu(arr, target):
        dp = [ [False for j in range(target+1)] for i in range(len(arr))]

        # make first column as True as we can form sum 0 with no elements taking
        for c in range(len(arr)):
            dp[c][0] = True

        # check if first element can be used for making up target
        first = arr[0]
        if first <= target:
            dp[0][first] = True

        for row in range(1, len(arr)):
            for col in range(1, target+1):
                # just take previous row value 
                notTaken = dp[row][col-1]

                taken = False
                if arr[row] <= col:
                    # pick and not pick
                    remainder = col - arr[row]
                    if dp[row-1][remainder] == True:
                        taken = True
                
                dp[row][col] = taken or notTaken
        return dp[len(arr)-1][target]
    # return tabu(arr, target)

    def spacy(arr, target):
        prev = [False for j in range(target+1)]
        # make first element as True as i can form sum 0 with no elements
        prev[0] = True

        # check if first element can be used for making up target
        first = arr[0]
        if first <= target:
            prev[first] = True

        for row in range(1, len(arr)):
            temp = [False for j in range(target+1)]
            temp[0] = True
            for col in range(1, target+1):
                # make first element as True as i can form sum 0 with no elements
                notTaken = prev[col]
                taken = False
                if arr[row] <= col:
                    # pick and not pick
                    remainder = col - arr[row]
                    if prev[remainder] == True:
                        taken = True
                
                temp[col] = taken or notTaken

            prev = temp
        return prev[-1]
    return spacy(arr, target)
arr = [1,2,1,4]
target = 5
print(subsetTarget(arr, target))

