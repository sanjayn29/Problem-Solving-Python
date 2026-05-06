class Solution(object):
  def groupAnagrams(self, strs):
    seen = {}
    for i in strs:
        word = list(i)
        word = sorted(word)
        key = str(word)
        if key not in seen:
            seen[key]=[]
        seen[key].append(i)
    return list(seen.values())