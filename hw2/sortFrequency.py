from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        
        s = Counter(s)
        
        sort_s = sorted(s, key = lambda x: -s[x])
        
        res = ""
        
        for key in sort_s:
            
            addRes = key * s[key]
            res += addRes
            
        return res