class Solution:
    def excelColumnNumber(self, s):
        #code here
        ans = 0
        for i in s:
            value = ord(i) - ord("A")+1
            ans = ans*26 + value
        return ans