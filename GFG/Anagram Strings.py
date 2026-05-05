#User function Template for python3
class Solution:
    def areAnagram(ob, s1, s2):
        # code here 
        s1=list(s1)
        s2=list(s2)
        s1=sorted(s1)
        s2=sorted(s2)
        return 1 if(s1==s2) else 0