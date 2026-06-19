class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = {}
        res=[]
        for i in nums:
            freq[i] = freq.get(i,0)+1

        for i,j in freq.items():
            if j == 1:
                res.append(i)
        return res