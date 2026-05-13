class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res =""
        for i in strs:
            l=len(i)
            res = res+str(l)+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        if len(s)==0:
            return []
        res = []
        l = len(s)
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            n = int(s[i:j])
            key=""
            start = j+1
            end = start+n
            key = s[start:end]
            res.append(key)
            i = end
        return res
