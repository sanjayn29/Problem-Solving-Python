#User function Template for python3

class Solution:
    
    def getSingle(self,arr):
        res = 0
        for i in arr:
            res = res ^ i
        return res  
        # code here
