class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        val = []
        for i in range(n):
            while len(val)!=0 and temperatures[i] > temperatures[val[-1]]:
                ind = val.pop()
                res[ind] = i-ind
            val.append(i)
        return res