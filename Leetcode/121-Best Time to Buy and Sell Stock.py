class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        pro = 0
        for i in prices:
            if min > i:
                min = i
            max = i - min
            if max > pro:
                pro = max
        return pro