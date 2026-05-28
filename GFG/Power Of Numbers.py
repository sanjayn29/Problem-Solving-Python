class Solution:
    def reverseexponentiation(self, n):
        # code here
        rev = str(n)
        rev = rev[::-1]
        rev = int(rev)
        return n**rev