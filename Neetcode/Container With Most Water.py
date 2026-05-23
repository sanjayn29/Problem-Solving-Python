class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxy = 0
        while( left < right):
            width = right - left
            hight = min(height[left],height[right])
            area = width * hight
            maxy = max(maxy,area)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return maxy