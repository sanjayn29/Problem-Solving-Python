 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,nums):
        #code here
        if len(nums)==0:
            return 0
        nums=sorted(nums)
        cur =1
        lon =1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                cur+=1
            else:
                cur=1
            lon = max(cur,lon)
        return lon