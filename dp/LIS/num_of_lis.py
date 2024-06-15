class Solution:
    def findNumberOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [1] * n
        cnt = [1] * n
        maxi = 1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
                    #  inherit
                    cnt[i] = cnt[j]
                elif nums[i] > nums[j] and dp[i] == dp[j]+1:
                    # increase
                    cnt[i] = cnt[i] + cnt[j]

            if dp[i] > maxi:
                maxi = dp[i]
        print(dp)
        print(maxi)   
        # iterate to find count of lis
        total_cnt = 0
        for i in range(n):
            if dp[i] == maxi:
                total_cnt += cnt[i]
        return total_cnt
    
ob = Solution()
nums = [1,3,5,4,7]
print(ob.findNumberOfLIS(nums))