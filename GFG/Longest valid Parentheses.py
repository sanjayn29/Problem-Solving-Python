
class Solution:
    def maxLength(self, s):
        # code here
        stack = []
        maxx = 0
        stack.append(-1)
        for i in range(len(s)):
            ch = s[i]
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                n = len(stack)
                if n==0:
                    stack.append(i)
                else:
                    maxx = max(maxx,i-stack[-1])
        return maxx