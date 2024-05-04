class Solution:
    def myAtoi(self, s: str) -> int:
        ans = "0"
        # step 1
        i = 0
        while s[i] == ' ':
            i = i + 1
        
        # step 2
        if s[i] == "-":
            ans = "-"
            i = i + 1
        elif s[i] == "+":
            ans = "+"
            i = i + 1

        # step 3
        while i<len(s) and s[i].isnumeric():
            ans = ans + s[i]
            i = i + 1
        # step 4
        if int(ans) < (-1 * 2**31):
            ans = (-1 * 2**31)
        elif int(ans) > (2**31 -1):
            ans = 2**31 -1
        return int(ans)
object = Solution()
# print(object.myAtoi("-91283472332"))
print(object.myAtoi("+-12"))

print(int("+1"))