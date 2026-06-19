class Solution:
    def reverse(self, x: int) -> int:
        negative = x<0
        x=abs(x)
        result=0
        while x > 0:
            result = (result*10)+x%10
            x //= 10
        if negative:
            result = -result
        if -2**31 <= result <= 2**31:
            return result
        else:
            return 0