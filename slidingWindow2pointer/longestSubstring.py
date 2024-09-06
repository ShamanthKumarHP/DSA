class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0
        dictKeys = {}
        maxi = float('-inf')
        while r < n:
            idx = dictKeys.get(s[r])
            if idx != None: # could be 0 also, so use properly
                # means already there, check if it is in my window
                if idx < l:
                    # not to consider, just update with current index
                    dictKeys[s[r]] = r
                else:
                    # it is in my window
                    dictKeys[s[r]] = r # update with current index
                    l = dictKeys[s[r]] + 1
            else:
                dictKeys[s[r]] = r
            maxi = max(maxi, (r-l+1))
            r = r+1
        return maxi
    
    def lengthOfLongestSubstringBest(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0
        dictKeys = [-1] * 255
        maxi = 0
        while r < n:
            idx = dictKeys[ord(s[r])]
            if idx != -1: 
                if idx >= l:
                    l = idx + 1
                
            dictKeys[ord(s[r])] = r
            maxi = max(maxi, (r-l+1))
            r = r+1
        return maxi

obj = Solution()
s="abcabcbb"
print(obj.lengthOfLongestSubstringBest(s))