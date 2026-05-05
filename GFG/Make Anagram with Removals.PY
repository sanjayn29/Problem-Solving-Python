class Solution:
    def remAnagram(self, s1, s2):
        # code here
        diff={}
        for i in s1:
            diff[i] = diff.get(i,0)+1
        for j in s2:
            diff[j] = diff.get(j,0)-1
            
        return sum(abs(k) for k in diff.values())