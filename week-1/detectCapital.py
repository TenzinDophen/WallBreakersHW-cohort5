class Solution:
    
    def isAllUpper(self, s):
        for i in s:
            if i.islower():
                return False
        return True
        
    def isAllLower(self, s):
        for i in s:
            if i.isupper():
                return False
        return True
        
    def detectCapitalUse(self, word: str) -> bool:
        if word == "":
            return True
        if word[0].isupper():
            if self.isAllUpper(word[1:]):
                return True
            elif self.isAllLower(word[1:]):
                return True
            else:
                return False
        else:
            if self.isAllLower(word[1:]):
                return True
            return False