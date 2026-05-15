class Solution:
    def isPalindrome(self, n):
		# code here
		n=str(n)
		res = ""
        for i in n:
            if i.isdigit():
                res+=i
        return res==res[::-1] 