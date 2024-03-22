def searchInsert(nums, target):
    low = 0
    high = len(nums)-1
    while (low <= high):
        mid = int((low+high)/2)
        if (target == nums[mid]):
            return mid
        elif (target > nums[mid]):
            low = mid+1
        elif (target < nums[mid]):
            high = mid-1
    return low
    

if __name__ == "__main__":
    print(searchInsert([1,3,5,6,11],4))
        