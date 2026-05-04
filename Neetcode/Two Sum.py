class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            balance = target - nums[i]

            if balance in seen:
                return [seen[balance],i]

            seen[nums[i]]=i

        return []