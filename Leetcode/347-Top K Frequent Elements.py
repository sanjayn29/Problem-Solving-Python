class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        op = {}
        res=[]
        for i in nums:
            op[i]=op.get(i,0)+1

        for _ in range(k):
            maxx = max(op.values())
            for i in op:
                if maxx == op[i]:
                    res.append(i)
                    del op[i]
                    break
        return res 