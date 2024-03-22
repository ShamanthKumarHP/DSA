#takes an alement and places in its correct position

# def insertion_sort(arr):
#     high = len(arr)

#     for i in range(1,high): 
#         for j in range(i): 
#             if arr[i-j] < arr [i - j - 1]: 
#                 temp = arr [i - j]
#                 arr[i - j] = arr [i - j - 1]
#                 arr [i - j - 1 ] = temp
#     return arr


def insertion_sort(arr):
    high = len(arr)

    for i in range(1,high): 
        for j in range(i,0,-1): 
            if arr[j] < arr [ j - 1]: 
                temp = arr [j]
                arr[j] = arr [j - 1]
                arr [j-1 ] = temp
    return arr

def insertion_recursion_1(arr, high=0):
    if high>=len(arr):
        return
    
    for i in range(high, 0, -1):
        if arr[i]<arr[i-1]:
            temp = arr[i]
            arr[i]= arr[i-1]
            arr[i-1] = temp

    insertion_recursion_1(arr,high+1)
    return arr

def swap(arr,high):
    if high <1:
        return arr
    if arr[high]<arr[high - 1]:
        temp = arr[high]
        arr[high] = arr[high -1 ]
        arr[high - 1] = temp

    return swap(arr,high-1)

def insertion_recursion_2(arr, high=0):
    if high > len(arr) - 1:
        return arr
    arr = swap(list(arr),high)
    return insertion_recursion_2(arr,high+1)

arr = [12,2,13,1,0]
# print(insertion_sort(arr))
# print(insertion_recursion_1(arr))
print(insertion_recursion_2(arr))

