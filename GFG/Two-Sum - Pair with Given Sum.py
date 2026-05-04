class Solution:
	def twoSum(self, nums, target):
	    seen = set()
		
		for num in nums:
		    balance = target-num
		    
		    if balance in seen:
		        return True
		        
		    seen.add(num)
		    
		return False