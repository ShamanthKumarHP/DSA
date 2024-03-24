#https://leetcode.com/problems/next-permutation/
def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # 1. Find left prefix -> break point 
    # 2. if no break point reverse the array
    # 3. if break point, 
    # find n who is next greater of breakpoint element and swap
    # 4. Arrange the right side in sorted way => Reverse

    i = len(nums) - 1 - 1
    break_idx = -1
    while i > -1:
        if nums[i] < nums[i + 1]:
            break_idx = i
            break
        i = i - 1

    if i == -1:
        nums.sort()
        return nums

    j = len(nums) -1
    while j > break_idx:
        if nums[j] > nums[break_idx]:
            nums[break_idx], nums[j] = nums[j], nums[break_idx]
            break
        j = j - 1
    
    m = break_idx + 1 
    n = len(nums) - 1
    mid_point = int((m+n)/2)
    while (m <= mid_point):
        nums[m], nums[n] = nums[n], nums[m]
        m = m + 1
        n = n - 1

    # nums[break_idx+1:] = nums[break_idx+1:][::-1]
    return (nums)
nums  = [1,2,3]
print(nextPermutation(nums))


