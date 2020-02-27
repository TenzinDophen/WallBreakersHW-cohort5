
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        mappingS = {}
        mappingT = {}
        
        arr = s.split(" ")
        
        if len(arr) != len(pattern):
            return False
        
        
        
        for i, c in enumerate(arr):
            if c in mappingS:
                if mappingS[c] != pattern[i]:

                    return False
            else:
                mappingS[c] = pattern[i]
            
            if pattern[i] in mappingT:
                if mappingT[pattern[i]] != c:

                    return False
            else:
                mappingT[pattern[i]] = c
            
        return True