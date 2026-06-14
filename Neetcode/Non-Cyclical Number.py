class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        if n < 10:
            return False
        happy = 0
        while n > 0:
            digit = n%10
            happy += digit*digit
            n = n//10
        return self.isHappy(happy)