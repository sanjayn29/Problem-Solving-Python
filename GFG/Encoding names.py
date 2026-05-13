#User function Template for python3

class Solution:
    def encodeTheName(self, S):
        # code here 
        res = ""
        sub = 10
        asci = 0
        for i in S:
            asci = ord(i)
            asci = asci - sub
            res = res + str(asci)
            sub-=1
        return res