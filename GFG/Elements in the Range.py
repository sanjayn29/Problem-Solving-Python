class Solution:
    def checkElements(self, start, end, arr):
        # code here
        seen = {}
        s=start
        while s<=end:
            if s not in arr:
                return False
            s=s+1
        return True