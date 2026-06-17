class Solution:
    def kokoEat(self, piles, h):
        # Code here
        low = 1
        high = max(piles)
        ans = high
        while low <= high:
            hour = 0
            mid = low + (high-low)//2
            for i in piles:
                hour += (i+mid-1)//mid
            if hour <= h:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans