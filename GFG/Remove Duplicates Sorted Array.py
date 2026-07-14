class Solution:
    def removeDuplicates(self, nums):
        # code here 
        new = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[new] = nums[i]
                new+=1
        return nums[:new]