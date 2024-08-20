class Solution:
    def minX(self, src, dest, arr):
        mod = 100000
        dist = [ 0 for i in range(mod)]
        q = []
        q.append((0,src))
        while q:
            numX, node = q.pop(0)
            for k in arr:
                new_num = (k * node) % mod
                # if numX + 1 < dist[new_num]:
                #     dist[new_num] = numX + 1
                #     if new_num == dest:
                #         return numX + 1
                #     q.append((numX+1, k*node))

                # just visit array
                if new_num == dest:
                    return numX + 1
                if dist[new_num] == 0:
                    dist[new_num] = 1
                    q.append((numX+1, new_num)) 
        return -1
    
obj = Solution()
src = 2
dest = 30
arr = [2,3,5]
print(obj.minX(src, dest, arr))