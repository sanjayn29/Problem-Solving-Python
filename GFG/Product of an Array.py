class Solution:
    # arr is the array
    def product(self, arr):
        # your code here
        summ = 1
        for i in arr:
            summ= summ*i%1000000007
        return summ
            