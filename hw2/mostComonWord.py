from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph, banned):
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
            
        count = Counter(
            word for word in paragraph.lower().split())

        sort_res = sorted(count, key = lambda x: -count[x])
        
        for key in sort_res:
            if key not in banned:
                return key