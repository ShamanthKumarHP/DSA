def halfSortedBS(arr, target):
    low = 0
    high = len(arr) - 1
    while high - low > 1:
        mid = int((low + high)/2)
        print ("mid", arr[mid])
        if (target == arr[mid]):
            return mid
       
        if arr [low] <= arr[mid]:
            if target < arr[mid] and target >= arr[low]:                        
                high = mid - 1
            else:
                low = mid + 1
        else:
            if target <= arr[high] and target > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1


    if target == arr[low]:
        return low
    elif target == arr[high]:
        return high

    return False

def ByFindingMin(arr):
    min_value = None
    low = 0
    high = len(arr) - 1
    if arr[low]<=arr[high]:
        return arr[low]
    while low<=high:
        mid = int((low+high)/2)

        if arr[mid]<arr[mid-1]:
            return arr[mid]
        if arr[mid]>arr[high]:
            low = mid+1
        else:
            high = mid - 1

    

    return min_value


if __name__ == "__main__":
    a1 = [5,1,1,1,1,2]
    aa = []
    a2 = [4,5,6,7,8,1,2,3]
    a3 = [3,5,0,1,2]
    a4 = [5,1,2,3]
    target = 1
    print(ByFindingMin(a1))
    #print(halfSortedBS(arr, target))

   
    # t = 1




