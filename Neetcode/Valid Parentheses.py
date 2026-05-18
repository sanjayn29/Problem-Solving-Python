class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '[' or i == '{' or i == '(':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                n = len(stack)
                peek = stack[n-1]
                if ( peek == '[' and i == ']') or ( peek == '{' and i == '}') or ( peek == '(' and i == ')'):
                    stack.pop()
                else:
                    return False
        return len(stack)==0