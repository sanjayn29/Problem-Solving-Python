class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            balance = target - nums[i]

            if balance in seen:
                return [seen[balance],i]

            seen[nums[i]]=i

        return []