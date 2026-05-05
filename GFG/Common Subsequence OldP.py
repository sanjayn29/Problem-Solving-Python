class Solution:
    def commonSubseq (ob, s1, s2):
        # code here 
        for i in s1:
            if i in s2:
                return 1
        return 0