from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t)
        
        dic = defaultdict(int)
        if len(s) != len(t):
            return False
        
        for i in s:
            dic[i] += 1
   
        for i in t:
            dic[i] -= 1
            if dic[i] < 0:
                return False
            
        return True