class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                i = i.lower()
                res+=i
        return res==res[::-1] 