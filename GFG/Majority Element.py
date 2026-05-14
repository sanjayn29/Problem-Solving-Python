class Solution:
    def majorityElement(self, arr):
        #code here
        maj = {}
        for i in arr:
            maj[i]=maj.get(i,0)+1
        res = max(maj.values())
        if res > len(arr)/2:
            return max(maj,key=maj.get)
        else:
            return -1
            