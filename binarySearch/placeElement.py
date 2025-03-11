arr = [1, 3, 4, 6, 10]

def findandinsert(arr, element):
    low = 0 
    high = len(arr) - 1

    while low<=high:
        mid = (low+high)//2

        if arr[mid] ==  element:
            return mid
        
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return high + 1

target = 0
print(findandinsert(arr, target))


    
    