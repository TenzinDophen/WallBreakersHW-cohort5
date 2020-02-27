class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        if not s:
            return True
        
        for i in t:
            if i == s[count]:
                count += 1
                if count >= len(s):
                    return True
        return False