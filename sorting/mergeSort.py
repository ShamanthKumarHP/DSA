# split to one and compare and make it one


def merge(arr, first_idx, mid, last_idx):
    i = first_idx
    j = mid+1
    new_list = []

    while (i<=mid and j <= last_idx):
        if arr[j]<=arr[i]:
            new_list.append(arr[j])
            j = j + 1
        else:
            new_list.append(arr[i])
            i = i + 1

    while i <= mid :
        new_list.append(arr[i])
        i = i + 1
    
    while j <= last_idx:
        new_list.append(arr[j])
        j = j + 1

    for i in range(first_idx, last_idx + 1):
        arr[i] = new_list[i - first_idx]

    return arr

def merge_sort(arr, first_idx, last_idx):

    if first_idx>=last_idx:
        return 

    mid = int((first_idx + last_idx)/2)

    merge_sort(arr, first_idx, mid)
    merge_sort(arr, mid + 1, last_idx)
    merge(arr, first_idx, mid, last_idx)
    return arr

arr = [4,3,1,2]
arr = [5,1,7,4,3]
print(merge_sort(arr, 0, len(arr)-1))

