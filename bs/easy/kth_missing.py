
def find_kth_integer(arr, k):
    # check how many elements is missing at a point
    # then adjust low and high as per required 
    # then find diff and add

    low = 0
    high = len(arr)-1
    while low <= high:
        mid = int((low+high)/2)
        print(low,mid,high)
        missing_count = arr[mid] - (mid + 1)
        # print("missing_count", missing_count )
        if missing_count < k:
            low = mid + 1
        else:
            high = mid - 1

    # val = arr[high] + (k - (arr[high] - high - 1)))
    
    val = k + high + 1
    return val

arr = [1,3,4,7]
arr1 = [1,2,3,4]
k = 3
print(find_kth_integer(arr1,  k))



