class Solution:
    def firstSearch(self, nums, target):
        # Code Here
        left = 0
        right = len(nums)-1
        ans = -1
        while(left <= right):
            mid = (left + right) / 2
            mid = int(mid)
            if(nums[mid] == target):
                ans =  mid
                right = right -1
            elif (nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        return ans 