class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [x for x in s]
        vowel = ['a', 'e', 'i', 'o', 'u']
        start = 0
        end = len(s)-1
        
        while(start < end):
            while(start < end and not s[start].lower() in vowel ):
                start += 1
            while(start < end and not s[end].lower() in vowel ):
                end -= 1
            
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
            
        return "".join(s)