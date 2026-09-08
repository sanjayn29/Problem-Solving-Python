class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wind1=0
        for i in range(k):
            wind1+=nums[i]
        wind2=wind1
        for i in range(k,len(nums)):
            wind1+=nums[i]
            wind1-=nums[i-k]
            wind2=max(wind1,wind2)
        return wind2/k