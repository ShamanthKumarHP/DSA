class Solution:
    def removeOuterParentheses(self, s):
        # using counter
        isOuter = 0
        ans = ""
        for i in s:
            if i == "(":
                if isOuter == 0:
                    isOuter += 1
                    pass
                else:
                    ans = ans + "("
                    isOuter += 1
            elif i == ")":
                isOuter -= 1
                if isOuter == 0:
                    pass
                else:
                    ans = ans + ")"
        return ans
    
    def removeOuterParentheses2(self, s):
        # using stack 
        stack = []
        ans = ""
        for i in s:
            if i == "(":
                if len(stack) == 0:
                    stack.append(i)
                else:
                    stack.append(i)
                    ans = ans + "("
            else:
                stack.pop()
                if len(stack) != 0:
                    ans = ans + ")"
        return ans
                



        

        



             
        