def simpleBS(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = int((low + high)/2)
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid -1 
        elif target > arr[mid]:
            low = mid+1
    return False