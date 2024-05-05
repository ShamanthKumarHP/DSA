class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dict
        # d = {a: [idx1, idx2], c: []}
        if len(s) <=1:
            return s
        # od = dict()
        # i = 0
        # max_length = 1
        # max_palind = s[0]
        # while i < len(s):
        #     occured = od.get(s[i], [])
        #     if occured:
        #         for k in occured:
        #             if i - k + 1  > max_length:
        #                 left = s[k:i+1]
        #                 right = s[i : k: -1] + s[k]
        #                 if left == right:
        #                     max_palind = s[k:i+1]
        #                     max_length = i+1 - k
        #         occured.append(i)
        #         od[s[i]] = occured
        #     else:
        #         od[s[i]] = [i]
            
        #     i = i + 1
        # return max_palind
        # TC: N * N
        # SC: N + N

        max_palindrome = s[0]
        for i in range(len(s)-1):
            # For odd length palindrome, we will consider the current character as the center and expand around it.
            left = i
            right = i
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left = left - 1
                right = right + 1
            if len(s[left+1: right]) > len(max_palindrome):
                max_palindrome = s[left+1: right]

            # For even length palindrome, we will consider the current character and the next character as the center and expand around it.
            left = i 
            right = i + 1
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left = left - 1
                right = right + 1
            if len(s[left+1: right]) > len(max_palindrome):
                max_palindrome = s[left+1: right]

        return max_palindrome

obj = Solution()
print(obj.longestPalindrome("babad"))
            
        