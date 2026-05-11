class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for _ in range(k):
            maxx = max(freq.values())
            for i in freq:
                if maxx == freq[i]:
                    res.append(i)
                    del freq[i]
                    break
        return res