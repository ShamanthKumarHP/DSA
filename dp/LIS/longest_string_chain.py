class Solution:
    def longestStrChain(self, words) -> int:
        def check_possibility(s1, s2):
            n1 = len(s1)
            n2 = len(s2)
            if n1-n2 != 1:
                return False

            i = 0 
            j = 0 
            while i < n1 :
                if j < n2 and s1[i] == s2[j]:
                    i = i + 1
                    j = j + 1
                else:
                    i = i + 1

            if i == n1 and j == n2:
                return True

            return False
        
        if not words:
            return 0
        
        n = len(words)
        dp = [1] * n
        maxi = -1
        words.sort(key = len)
        for i in range(1, n):
            for j in range(i):
                if check_possibility(words[i], words[j]) and dp[j]+1 > dp[i]:
                    dp[i] =  dp[j] + 1
            if dp[i] > maxi:
                maxi = dp[i]
        return maxi
        
a = Solution()
print(a.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))