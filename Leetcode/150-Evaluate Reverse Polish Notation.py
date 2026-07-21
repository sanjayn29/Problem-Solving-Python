class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for i in range(len(tokens)):
            if tokens[i]=="*":
                a = res.pop()
                b = res.pop()
                ans = a*b
                res.append(ans)
            elif tokens[i]=="+":
                a = res.pop()
                b = res.pop()
                ans = a+b
                res.append(ans)
            elif tokens[i]=="-":
                a = res.pop()
                b = res.pop()
                ans = b-a
                res.append(ans)
            elif tokens[i]=="/":
                a = res.pop()
                b = res.pop()
                ans = int(b/a)
                res.append(ans)
            else:
                temp=int(tokens[i])
                res.append(temp)
        return res.pop()