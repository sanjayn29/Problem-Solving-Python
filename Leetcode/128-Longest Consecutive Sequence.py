class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        nums=sorted(nums)
        cur =1
        lon =1
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]):
                continue
            if(nums[i]==nums[i-1]+1):
                cur+=1
            else:
                cur=1
            lon = max(lon,cur)
        return lon        