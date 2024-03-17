# def remove_dup(arr):
#     s = set()
#     for i in arr:
#         s.add(i)
#     return s

def remove_dup(arr):
    i = 0
    j = 1
    while (j < len(arr)):
        if arr[j] != arr[i]:
            i = i + 1
            arr[i] = arr[j]
        j = j + 1
    print(arr[:i+1])
    return i+1




arr = [1,1,2,3,3,4]
print(remove_dup(arr))