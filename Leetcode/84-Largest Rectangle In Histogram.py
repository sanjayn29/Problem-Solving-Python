class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        n = len(heights)
        for i in range(n+1):
            curr = 0 if i==n else heights[i]
            while stack and curr < heights[stack[-1]]:
                height = heights[stack.pop()]
                left = -1 if not stack else stack[-1]
                width = i - left -1
                maxarea = max(maxarea,height*width)

            stack.append(i)
        return maxarea