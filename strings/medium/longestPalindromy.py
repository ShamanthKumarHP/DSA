class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dict
        # d = {a: [idx1, idx2], c: []}

        od = dict()
        i = 0
        max_length = 0
        max_palind = ""
        while i < len(s):
            occured = od.get(s[i], [])
            if occured:
                for k in occured:
                    left = s[k:i+1]
                    right = s[i : k: -1] + s[k]
                    if left == right:
                        if i+1 - k > max_length:
                            max_palind = s[k:i+1]
                            max_length = i+1 - k
                occured.append(i)
                od[s[i]] = occured
            else:
                od[s[i]] = [i]
            
            i = i + 1
        return max_palind


object = Solution()
print(object.longestPalindrome("aabaa"))
# s = "abc"
# print(s[2:-1:-1])