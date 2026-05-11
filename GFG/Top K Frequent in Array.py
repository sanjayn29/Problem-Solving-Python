class Solution:
	def topKFreq(self, arr, k):
		# Code here
		op = {}
		for i in arr:
		    op[i]=op.get(i,0) + 1
		    
		keys = sorted(op.keys(), key=lambda x: (-op[x], -x))
        return keys[:k]