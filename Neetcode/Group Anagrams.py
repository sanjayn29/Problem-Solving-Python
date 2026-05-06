class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            word = list(i)
            word = sorted(i)
            key = str(word)
            if key not in seen:
                seen[key]=[]
            seen[key].append(i)
        return list(seen.values())
        