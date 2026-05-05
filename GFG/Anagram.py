class Solution:
    def areAnagrams(self, s1, s2):
       # code here
       s1=list(s1)
       s2=list(s2)
       s1=sorted(s1)
       s2=sorted(s2)
       return s1==s2