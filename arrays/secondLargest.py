def secondLargest(arr):
    first_large = arr[0]
    secondar_large = -1

    for i in arr:
        if i == first_large:
            continue
        elif i > first_large:
            secondar_large = first_large
            first_large = i
        elif i > secondar_large:
            secondar_large = i
    return secondar_large

def secondSmallest(arr):
    first_small = arr[0]
    second_small = arr[0]
    for i in arr:
        if i == first_small:
            continue
        elif i < first_small:
            second_small = first_small
            first_small = i
        elif i < second_small:
            second_small = i
    return second_small

arr = [2,3,1,4,7,7,6]
sl = secondLargest(arr)
ss = secondSmallest(arr)
print(sl, ss)

