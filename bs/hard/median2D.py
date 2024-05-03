# https://takeuforward.org/data-structure/median-of-row-wise-sorted-matrix/

def upperBound(arr, k):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        mid = int((low+high)/2)
        if arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return low


def countSmallerThanOrEqualMid(nums, mid):
    count = 0
    for row in nums:
        count = count + upperBound(row, mid)
    return count

def findMedian(nums):
    m = len(nums)
    n = len(nums[0])
    required = int((m*n)/2) # required_count > required_idx

    low = 1
    high =  10**9

    while low <= high:
        mid = int((low+high)/2)
        
        check = countSmallerThanOrEqualMid(nums, mid)
        if check <= required:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1   
    return low

nums = [[1, 2, 2],[2,5, 5], [7, 7, 9]]
print(findMedian(nums))