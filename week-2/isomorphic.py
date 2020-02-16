class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mappingS = {} 
        mappingT = {}
        
        for i, c in enumerate(s):
            if c in mappingS:
                if mappingS[c] != t[i]:
                    return False
            else:
                mappingS[c] = t[i]
            
            if t[i] in mappingT:
                if mappingT[t[i]] != c:
                    return False
            else:
                mappingT[t[i]] = c
            
        return True