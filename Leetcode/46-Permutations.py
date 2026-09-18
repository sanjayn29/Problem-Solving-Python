class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        cur = []
        used = [False]*len(nums)
        self.backtracking(nums,res,cur,used)
        return res
    
    def backtracking(self,nums,res,cur,used):
        if len(cur) == len(nums):
            res.append(cur.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            cur.append(nums[i])
            used[i]=True
            self.backtracking(nums,res,cur,used)
            del cur[-1]
            used[i]=False                  