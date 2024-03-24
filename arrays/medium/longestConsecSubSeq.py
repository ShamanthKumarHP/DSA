
# https://leetcode.com/problems/longest-consecutive-sequence/
def longestConsecutive(nums):
    d = dict()
    for i in nums:
        d[i] = 1

    maxCnt = 0
    for i in d.keys():
        j = i
        cnt = 1
        if not d.get(j-1,0):
            j = j + 1
            while d.get(j,0):
                cnt = cnt + 1
                j = j + 1
            maxCnt = max(maxCnt, cnt)
    return maxCnt

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))

# when i'm in k, check if k - 1 exists, dont start search from 4,3,2
# if doesnt exits, then assume thats the first element and check for next elements
# tc= n for dict, maximum it will take 2n inside for loop.
# so TC = 3N, SC = N

