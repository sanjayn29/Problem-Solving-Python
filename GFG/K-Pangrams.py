#User function Template for python3
class Solution:
  def kPangram(self,string, k):
    # code here
    seen = set()
    n = 0 
    for i in string:
        if i != ' ':
            if i not in seen:
                seen.add(i)
            n=n+1
    if n<26:
        return False
    
    if (26-len(seen)) <= k:
        return True
        
    return False
    