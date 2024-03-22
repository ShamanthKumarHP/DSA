#move the largest element to last by comparing i and i + 1
def bubbleSort(arr):
    high = len(arr)

    for i in range(high):
        for j in range(high-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    
    return arr

def bubble_recursion_1(arr, high, last):
    if last>=high:
        return arr
    for j in range(high-last):
        if arr[j] > arr[j+1]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
    
    return bubble_recursion_1(arr,high,last+1)

def find_and_swap(arr,i,j,high):
    if j+1>high:
        return arr
    if arr[i] < arr[j]:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    return find_and_swap(arr,i+1,j+1,high)

def bubble_recursion_2(arr, high,last):
    if last>=high:
        return arr
    find_and_swap(arr,0,0,high)
    return bubble_recursion_2(arr,high,last+1)
        

arr = [1,4,1,2,0]
print(bubbleSort(arr))
print(bubble_recursion_1(arr, len(arr),1))
print(bubble_recursion_2(arr, len(arr),1))