#User function Template for python3

class Solution:
	def singleNum(self, nums):
		# Code here
		freq = {}
        res=[]
        for i in nums:
            freq[i] = freq.get(i,0)+1

        for i,j in freq.items():
            if j == 1:
                res.append(i)
        res = sorted(res)
        return res
