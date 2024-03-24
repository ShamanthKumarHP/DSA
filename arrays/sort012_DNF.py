# https://leetcode.com/problems/sort-colors/description/
def sort012(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low] , nums[mid] = nums[mid], nums[low]
            low = low + 1
            mid = mid + 1
        elif nums[mid] == 1:
            mid = mid + 1
        elif nums[mid] == 2:
            nums[high] , nums[mid] = nums[mid], nums[high]
            high = high - 1
    return nums

nums = [2,0,2,1,1,0]
print(sort012(nums))

# 0 to low - 1 should be 0s
# low to mid - 1 should be 1s
# mid to high  should be unsorted (0,1,2)
# high+1 to n - 1 should be 2s

# as i will be sorting from left, so when i get nums[mid] == 0, i have to increase low and mid. 
# because in coming element will be always 1
# but when i swap with high, then i should not increase mid because i'm yet to place that element.
# because in coming element might be 0,1,2