class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, arr):
        # code here
        pro = 0
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                pro = pro + arr[i]-arr[i-1]
        return pro