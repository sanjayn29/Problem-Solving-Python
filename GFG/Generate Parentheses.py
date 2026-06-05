class Solution:
    def generateParentheses(self, n):
        #code here
        res = []

        def backtracking(res,curr,openn,close,n):
            if len(curr)==n*2:
                res.append(curr)
                return
            if openn < n:
                backtracking(res,curr+"(",openn+1,close,n)
            if close < openn:
                backtracking(res,curr+")",openn,close+1,n) 

        backtracking(res, "",0,0,n/2)
        return res
