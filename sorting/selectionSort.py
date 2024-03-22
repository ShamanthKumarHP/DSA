# Selection sort
# find min and move it to left of the array

def selection_sort(arr):
    high = len(arr) 
    for i in range(0,high):
        min_idx = i
        for j in range(i,high):
            if arr[j]<=arr[min_idx]:
                min_idx = j
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
    return arr

def selection_sort_recursion(arr, low, high):

    int_min = arr[low]
    idx = low
    i = low
    
    if high<=low:
        return arr
    
    while (i <= high):
        if arr[i] < int_min :
            int_min = arr [i]
            idx = i
        i = i + 1
    arr[low], arr[idx] = arr [idx], arr[low]
    
    selection_sort_recursion(arr, low+1, high)
    return arr

arr = [3,4,1,2,0]
print(selection_sort(arr))
print(selection_sort_recursion(arr, 0, len(arr)-1))