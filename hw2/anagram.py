from collections import Counter, defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        result = []
        lenP = len(p)
        if lenP > len(s):
            return result
        
        mappingP = Counter(p)
        mappingS = Counter(s[:lenP])
        
        firstChar = 0
        
        for i in range(lenP, len(s)):
            if mappingS == mappingP:
                result.append(firstChar)
            c = s[firstChar]
            mappingS[c] -= 1
            if mappingS[c] == 0:
                del mappingS[c]
            firstChar += 1
            mappingS[s[i]] += 1
            
        if mappingS == mappingP:
            result.append(firstChar)
        
        return result