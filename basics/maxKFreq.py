
def giveFreq(nums,k,i):
    n = i -1
    cnt = 1
    while k>0 and n>=0:
        diff = nums[i] - nums[n]
        if diff <=k:
            k = k - diff
            cnt = cnt+1
            n = n-1
        else:
            break
    return cnt

def maxFrequency( nums, k):
    nums.sort()
    i = len(nums)
    maxFreq = 1
    while i>=0:
        cnt = giveFreq(nums[:i],k,i-1)
        i = i -1
        if cnt > maxFreq:
            maxFreq = cnt
    return maxFreq

nums = [3,4,6,7]
k = 2
print(maxFrequency(nums,k))
        