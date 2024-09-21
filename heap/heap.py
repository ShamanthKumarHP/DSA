class Solution:
    def topKFrequent(self, nums, k: int):
        # solution 1
        n = len(nums)
        bucket = [[] for i in range(n+1)] # to maintain nums at its freq index
        hash_map = {} # {num: freq}
        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1
        
        for key, freq in hash_map.items():
            bucket[freq].append(key)
        print(bucket)
        ans = []
        i = n
        while i >= 0:
            if k == 0:
                break
            if bucket[i]:
                ans.extend(bucket[i])
                k = k - 1
            i = i - 1
        return ans




obj = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(obj.topKFrequent(nums, k))
