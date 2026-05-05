class Solution:
    def countWords(self, List):
        #code here
        seen={}
        for i in List:
            seen[i]=seen.get(i,0)+1;
        op = 0
        for i in seen:
            if seen[i] == 2:
                op=op+1
        return op