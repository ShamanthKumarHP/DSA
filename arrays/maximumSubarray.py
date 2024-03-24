# https://leetcode.com/problems/maximum-subarray/description/


def maxSubArray(nums):
    # maxi = float('-inf')
    # sum = 0
    # for i in nums:
    #     sum = sum + i
    #     if sum > maxi:
    #         maxi = sum
    #     if sum < 0:
    #         sum = 0
    # return maxi

    # in case if they ask subarray to return
    # then keep track of start point and end point

    maxi = float('-inf')
    sum = 0
    for idx, i in enumerate(nums):
        if sum == 0:
            start = idx
        sum = sum + i
        if sum > maxi:
            maxi = sum
            end = idx
        if sum < 0:
            sum = 0
        print(start, end)
    return nums[start: end+1]
# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-2,-3,-1,-1]
print(maxSubArray(nums))
