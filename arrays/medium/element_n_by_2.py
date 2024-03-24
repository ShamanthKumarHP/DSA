#Moore’s Voting Algorithm:
#https://leetcode.com/problems/majority-element/description/
def majorityElement(nums):
    c = 0
    m = 0
    i = 0
    while i < len(nums):
        if c == 0:
            m = nums[i]
            c = c + 1
        elif nums[i] == m:
            c = c+1
        else:
            c = c -1 
        i = i + 1
    return m

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))