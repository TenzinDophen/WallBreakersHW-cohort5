from collections import Counter, defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        result = []
        lenP = len(p)
        if lenP > len(s):
            return result
        s = list(s)
        p = list(p)
        
        s_sort = sorted(s[:lenP])
        
        
        
        return result