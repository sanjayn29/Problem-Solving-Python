class Solution(object):
    def containsDuplicate(self, nums):
        seen={}
        for i in nums:
            seen[i]=seen.get(i,0)+1
        for i in nums:
            if seen.get(i) > 1:
                return True
        return False