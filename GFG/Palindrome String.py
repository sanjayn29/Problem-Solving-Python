class Solution:
    def isPalindrome(self, s):
        # code here
		res = ""
        for i in s:
            if i.isalpha():
                res+=i
        return res==res[::-1] 
