#User function Template for python3

class Solution:
    def isSumPalindrome (self, n):
        if str(n) == str(n)[::-1]:
            return n
            
        for i in range(5):

            rev = int(str(n)[::-1])

            s = n + rev

            if str(s) == str(s)[::-1]:
                return s

            n = s

        return -1