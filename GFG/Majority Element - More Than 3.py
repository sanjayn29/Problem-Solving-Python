class Solution:
    def findMajority(self, arr):
        # code here
        maj = {}
        for i in arr:
            maj[i]=maj.get(i,0)+1
        res = max(maj.values())
        return sorted([k for k , v in maj.items() if v > len(arr)/3])