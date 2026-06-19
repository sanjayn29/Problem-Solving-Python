class Solution:
    def isPowerofTwo(self, n):
        # code here
        return True if n>0 and n&(n-1)==0 else False