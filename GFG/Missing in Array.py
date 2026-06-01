class Solution:
    def missingNum(self, nums):
        # code here
        n = len(nums)+1
        total = n*(n+1)/2
        now = sum(nums)
        return int(total-now)