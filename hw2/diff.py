from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mapS = Counter(s)
        mapT = Counter(t)
        
        for key in mapS:
            mapT[key] -= mapS[key]
            if mapT[key] == 0:
                del mapT[key]
         
        res = ""
        for key in mapT:
            res += key
            
        return res