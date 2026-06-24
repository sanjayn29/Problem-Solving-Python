# function for adding one to number 
class Solution:
    # Function to add one to a number represented as an array
    def addOne(self, arr):
        # code here
        n = len(arr)
        for i in range(n-1,-1,-1):
            if arr[i] < 9:
                arr[i]=arr[i]+1
                return arr
            arr[i]=0
        return [1]+arr