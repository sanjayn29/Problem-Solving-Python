class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_arr = arr[-1]
        arr[-1]=-1
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>max_arr:
                temp = max_arr
                max_arr = arr[i]
                arr[i] = temp
            else:
                arr[i]=max_arr
        return arr