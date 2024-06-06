class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def recursion(idx, subs):
            if subs == t[::-1]:
                return 1
            
            if idx == 0:
                if subs + s[idx] == t[::-1]:
                    return 1
                else:
                    return 0

            return recursion(idx-1, subs) + recursion(idx-1, subs+s[idx])
        return recursion(len(s)-1, "")
        
a = Solution()
print(a.numDistinct(s = "rabbbit", t = "rabbit"))