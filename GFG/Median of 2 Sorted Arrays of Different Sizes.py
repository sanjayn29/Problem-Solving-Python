class Solution:
    def medianOf2(self, a, b):
        # code here
        arr = a+b
        arr.sort()
        n = len(arr)
        if n%2==1:
            return arr[n//2]
        return (arr[n//2]+arr[n//2-1])/2