import bisect
def lower_bound(arr, target):
    low = 0
    high = len(arr)-1
    ans = 0
    while (low<=high):
        mid = int((low+high)/2)
        if arr[mid] >= target:
            ans = high
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
    return ans

def lis_bs(arr):
    temp = []
    temp.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] > temp[-1]:
            temp.append(arr[i])
        else:
            # pos = bisect.bisect_left(temp, arr[i])
            pos = lower_bound(temp, arr[i])
            temp[pos] = arr[i]
        
    return len(temp)

arr = [1,2,10,3,0,4]
print(lis_bs(arr))
