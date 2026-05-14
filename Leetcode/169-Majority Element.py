class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = {}
        for i in nums:
            maj[i]=maj.get(i,0)+1
        return max(maj,key=maj.get)