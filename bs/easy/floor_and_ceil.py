# lower bound = nearest number which is >= X
# upper bound = nearest number which is > X
# floor = largest number which is <=X
# ceil = smallest number which is >=X


def upperBound(arr, target):
    low = 0
    high = len(arr) - 1
    ans = len(arr)
    while low <= high:
        mid = int((low+high)/2)
        if arr[mid] > target:
            ans = mid
            high = mid - 1 
        else:
            low = mid + 1
    return ans

def lowerBound(arr, target):
    low = 0
    high = len(arr) - 1
    ans = len(arr)
    while low <= high:
        mid = int((low+high)/2)
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def floor(arr, target):
    low = 0 
    high = len(arr) - 1
    ans = len(arr)
    while (low <= high):
        mid = int((low+high)/2)
        if arr[mid] <= target:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

def ceil(arr, target):
    low = 0 
    high = len(arr) - 1
    ans = len(arr)
    while (low <= high):
        mid = int((low+high)/2)
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

arr1 = [10,30,40,50]
target1 = 45
print(upperBound(arr1, target1))
print(lowerBound(arr1, target1))
print(floor(arr1, target1))
print(ceil(arr1, target1))