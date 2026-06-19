#User function Template for python3

class Solution:
	def reverseDigits(self, x):
		# Code here
		negative = x<0
        x=abs(x)
        result=0
        while x > 0:
            result = (result*10)+x%10
            x //= 10
        if negative:
            result = -result
        return result