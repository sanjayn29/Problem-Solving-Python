#User function Template for python3
class Solution:
	def setBits(self, n):
		# code here
		res = 0
		while n > 0:
		    res += (n & 1)
		    n = n >> 1
		return res