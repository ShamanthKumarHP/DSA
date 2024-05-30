class Solution:
    def minimumDifference(self, nums):
        def spacy():
            totalSum = sum(nums)
            # finding half of the total sum, whether we can form subset of that
            # it total is odd, then we cannot have two equal halves

            # base case
            # first column ie sum 0, Make as True
            prev = [False for i in range(totalSum+1)]
            prev[0] = True
                
            if nums[0] <= totalSum:
                prev[nums[0]] = True
            
            for i in range(1, len(nums)):
                curr = [False for i in range(totalSum+1)]
                curr[0] = True
                for j in range(1, totalSum+1):
                    # not take
                    notTake = prev[j]

                    # take
                    take = False
                    if nums[i] <= j:
                        remainder = j - nums[i]
                        take = prev[remainder]

                    curr[j] = notTake or take
                prev = curr

            mini = int(1e9)
            i = 0
            middle = len(prev)//2
            while i < middle+1:
                if prev[i]:
                    partition1 = i
                    partition2 = totalSum - partition1
                    mini = min(mini, abs(partition1 - partition2))
                i = i + 1

            return mini

        return spacy()

ob = Solution()
print(ob.minimumDifference([3,9,7,3]))