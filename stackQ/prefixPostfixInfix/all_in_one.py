class Conversions:

    def get_associativity(self, sign):
        # Note
        # all operators will have L to R precedence in general except ^
        # during infix->postfix, we will pop elements if it has equal or greater precedence (L->R)
        # but for not for ^, we will pop if it has greater precedence element (which wont be there :)
        # 
        # during infix->postfix, since we reverse the string, we will pop elements if it has greater precedence (R->L)
        # but for ^, we will pop elements if it is greater than or equal precedence (L->R)
        # Because at last we will reverse the string

        if sign == '^': # has R->L associativity
            return 'R'
        return 'L'
    
    def get_precedence(self, sign):
        if sign == '^':
            return 3
        elif sign == '*' or sign == '/':
            return 2
        elif sign == '+' or sign == '-':
            return 1
        else:
            return -1

    def infix_to_postfix(self, equation):
        stack = []
        ans = ''
        for char in equation:
            if (ord(char) >= ord('a') and ord(char) <= ord('z') ) or \
                            (ord(char) >= ord('A') and ord(char) <= ord('Z')):
                ans += char
            else:
                if char == '(':
                    stack.append('(')
                elif char == ')':
                    # pop until u find (
                    while stack[-1] != '(':
                        ans = ans + stack.pop()
                    stack.pop() # we dont want ( 
                else:
                    while stack and \
                                (self.get_precedence(char) <= self.get_precedence(stack[-1])) \
                                and (self.get_associativity(char) == 'L'):
                            ans = ans + stack.pop()
                        # all operators will have L to R precedence in general, except ^
                    stack.append(char)
        while stack:
            ans = ans + stack.pop()
        return ans
    
    def infix_to_prefix(self, equation):
        # 1. reverse also interchange brackets
        # 2. apply conditional postifix, refer get_precedence
        # 3. reverse
        rev_equation = ''
        for i in range(len(equation)-1, -1, -1):
            if equation[i] == '(':
                rev_equation += ')'
            elif equation[i] == ')':
                rev_equation += '('
            else:
                rev_equation += equation[i]
        
        ans = ''
        stack = []
        for char in rev_equation:
            if (ord(char) >= ord('a') and ord(char) <= ord('z') ) or \
                            (ord(char) >= ord('A') and ord(char) <= ord('Z')):
                ans += char
            else:
                if char == '(':
                    stack.append('(')
                elif char == ')':
                    # pop until u find (
                    while stack[-1] != '(':
                        ans = ans + stack.pop()
                    stack.pop() # we dont want ( 
                else:
                    if char == '^':
                        while stack and self.get_precedence(stack[-1]) >= self.get_precedence(char):
                            ans += stack.pop()
                    else:
                        while stack and self.get_precedence(stack[-1]) > self.get_precedence(char):
                            ans += stack.pop()
                    stack.append(char)
        while stack:
            ans = ans + stack.pop()
        
        return ans[::-1]
    
    def postfix_to_infix(self, equation):
        equation = self.infix_to_postfix(equation)
        stack = []
        for char in equation:
            if (ord(char) >= ord('a') and ord(char) <= ord('z') ) or \
                            (ord(char) >= ord('A') and ord(char) <= ord('Z')):
                stack.append(char)
            else:
                firstTop = stack.pop()
                secondTop = stack.pop()
                stack.append('(' + secondTop + char + firstTop + ')')
        return stack.pop() # for valid expression
    
    def prefix_to_infix(self, equation):
        equation = self.infix_to_prefix(equation)
        stack = []
        for char in equation[::-1]:
            if (ord(char) >= ord('a') and ord(char) <= ord('z') ) or \
                            (ord(char) >= ord('A') and ord(char) <= ord('Z')):
                stack.append(char)
            else:
                firstTop = stack.pop()
                secondTop = stack.pop()
                stack.append('(' + firstTop + char + secondTop + ')')
        return stack.pop() # for valid expression

    def postfix_to_prefix(self, equation):
        equation = self.infix_to_postfix(equation)
        stack = []
        for char in equation:
            if (ord(char) >= ord('a') and ord(char) <= ord('z') ) or \
                            (ord(char) >= ord('A') and ord(char) <= ord('Z')):
                stack.append(char)
            else:
                firstTop = stack.pop()
                secondTop = stack.pop()
                stack.append(char+ secondTop + firstTop)
        return stack.pop() # for valid expression
    
    def prefix_to_postfix(self, equation):
        equation = self.infix_to_prefix(equation)
        stack = []
        for char in equation[::-1]:
            if (ord(char) >= ord('a') and ord(char) <= ord('z') ) or \
                            (ord(char) >= ord('A') and ord(char) <= ord('Z')):
                stack.append(char)
            else:
                firstTop = stack.pop()
                secondTop = stack.pop()
                stack.append(firstTop + secondTop + char)
        return stack.pop() # for valid expression


equation = "a+b*(c^d-e)"
obj = Conversions()
print("original expression ", equation)
print("infix_to_postfix: ", obj.infix_to_postfix(equation))
print("infix_to_prefix: ", obj.infix_to_prefix(equation))
print("postfix_to_infix: ", obj.postfix_to_infix(equation))
print("prefix_to_infix: ", obj.prefix_to_infix(equation))
print("postfix_to_prefix: ", obj.postfix_to_prefix(equation))
print("prefix_to_postfix: ", obj.prefix_to_postfix(equation))