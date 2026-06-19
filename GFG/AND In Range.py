class Solution:
	def andInRange(self, l, r):
		# code here
		res = 0
		while l<r:
		    l >>= 1
		    r >>= 1
		    res += 1
		return l<<res