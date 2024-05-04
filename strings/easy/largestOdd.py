class Solution:
    def largestOddNumber(self, num: str) -> str:
        if len(num) == 0:
            return ""
        i = len(num) - 1
        while i >= 0:
            if (int(num[i]) % 2 )!= 0:
                return num[:i+1]
            i = i - 1
        return ""
        
obj = Solution()
print(obj.largestOddNumber("52"))