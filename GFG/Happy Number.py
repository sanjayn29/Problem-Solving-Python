#User function Template for python3
class Solution:
    def isHappy (self, n):
        # code here
        if n == 1 or n == 7:
            return 1
        if n < 10:
            return 0
        happy = 0
        while n > 0:
            digit = n%10
            happy += digit*digit
            n = n//10
        return self.isHappy(happy)