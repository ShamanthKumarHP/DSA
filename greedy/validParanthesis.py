class Solution:
    def checkValidString(self, s: str) -> bool:
        def recursion(i, cnt):
            if i == len(s):
                if cnt == 0:
                    return True
                else:
                    return False
            if s[i] == '(':
                return recursion(i+1, cnt+1)
            elif s[i] == ')':
                if cnt == 0:
                    return False
                return recursion(i+1, cnt - 1)
            elif s[i] == '*':
                takeOpen = recursion(i+1, cnt+1)
                notTake = recursion(i+1, cnt)
                takeClose = False
                if cnt != 0:
                    takeClose = recursion(i+1, cnt-1)
                return takeOpen or notTake or takeClose
        return recursion(0,0)
        
        
obj = Solution()
s = '(*)'
print(obj.checkValidString(s))