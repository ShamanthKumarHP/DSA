# to find frequency of target in sorted array

def lowerBound(arr, target):
    low = 0
    high = len(arr) - 1
    lower_bound = -1
    while low <= high:
        mid = int((low+high)/2)
        if target == arr[mid]:
            lower_bound = mid
            high = mid -1
        elif target >  arr[mid]:
            low = mid+1
        elif target < arr[mid]:
            high = mid - 1
    return lower_bound

def upperBound(arr, target):
    low = 0
    high = len(arr) - 1
    upper_bound = -1
    while low<=high:
        mid = int((low+high)/2)
        if target == arr[mid]:
            low = mid+1
            upper_bound = mid
        elif target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
    return upper_bound


arr = [3,5,6,0,1,2]
target = 3
lb = lowerBound(arr, target)
ub = upperBound(arr, target)
if lb != -1 and ub != -1:
    print ("Frequency:" ,ub - lb+1 )
else:
    print("Element doesnt")