def quickSort(arr,low, high):
    if high - low <= 0:
        return
    
    pivot = arr[low]
    i = low
    j = high

    while (i<j):
        while (arr[i] <= pivot and i <= high):
            i = i + 1
        while (arr[j] > pivot and j >=0):
            j = j - 1
        if(i < j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    
    temp2 = arr[low]
    arr[low] = arr[j]
    arr[j] = temp2

    partition = j

    quickSort(arr, low, partition-1)
    quickSort(arr, partition+1, high)
    return arr
        
        
arr = [4,6,2,5,7,9,1,3]

print(quickSort(arr, 0, len(arr)-1))


