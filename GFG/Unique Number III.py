#User function Template for python3

class Solution:
    def getSingle(self, nums):
        # code here 
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1

        for i,j in freq.items():
            if j == 1:
                return i