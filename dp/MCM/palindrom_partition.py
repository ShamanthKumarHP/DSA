class Solution:
    

    def minCut(self, s: str) -> int:
        dp = [-1 for i in range(len(s))]

        def isPalindrom(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        def recursion(i):
            if i == len(s):
                return 0

            if dp[i] != -1:
                return dp[i]

            mini = 2000
            for k in range(i, len(s)):
                if isPalindrom(i,k):
                    cnt = 1 + recursion(k+1)
                    mini = min(cnt, mini)
            dp[i] = mini
            return dp[i]
        
        return recursion(0) - 1

        
ob = Solution()
print(ob.minCut("ab"))
s = "abcce"
print(s[1:0:-1])
print(s[1:-1:-1])
print(s[2:1:-1])
print(s[-1])

print(s[0:1] == s[0::-1])

