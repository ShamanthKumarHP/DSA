def msc(arr1, arr2, k):
    import heapq
    arr1 = sorted(arr1, reverse=True)
    arr2 = sorted(arr2, reverse=True)
    print(arr1, arr2)
    heap = []
    visited = set()
    heapq.heappush(heap, (-(arr1[0] + arr2[0]), (0,0)))# obviously first max sum
    visited.add((0,0))
    ans = []
    while k and heap:
        val, (x,y) = heapq.heappop(heap)
        ans.append(-1*val)
        if y + 1 < len(arr2):
            if (x, y+1) not in visited:
                heapq.heappush(heap, (-(arr1[x]+arr2[y+1]),(x, y+1)))
                visited.add((x,y+1))
        if x + 1 < len(arr1):
            if (x+1, y) not in visited:
                heapq.heappush(heap, (-(arr1[x+1]+arr2[y]), (x+1,y)))
                visited.add((x+1,y))
        k=k-1

    return ans

arr1 = [4,2,3,1]
arr2 = [5,6,2,1]
print(msc(arr1, arr2, k=4))