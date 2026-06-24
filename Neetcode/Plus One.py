class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0
        for i in digits:
            ans = (ans*10)+i
        ans = ans+1
        res = []
        while ans > 0:
            n = ans%10
            ans = ans//10
            res.append(n)
        return res[::-1]