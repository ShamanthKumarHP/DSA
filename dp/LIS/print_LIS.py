nums = [100,15,30, 9, 40, 1]
# data = {0: 0, 1:1, 2:2, 3:3, 4:4}
def lis(nums):
    n = len(nums)
    dp = [1] * n

    data = {}
    last_idx = 0
    maxi = 0
    for i in range(n):
        data[i] = i
        for prev_idx in range(i):
            if nums[i] > nums[prev_idx] and dp[prev_idx]+1 > dp[i]:
                    dp[i] = dp[prev_idx]+1
                    data[i] = prev_idx

        if dp[i] > maxi:
            maxi = dp[i]
            last_idx = i
            
    print(nums[last_idx])
    while (last_idx  != data[last_idx]):
        print(nums[data[last_idx]])
        last_idx = data[last_idx]


    print(data)
    return max(dp)
    

print(lis(nums))