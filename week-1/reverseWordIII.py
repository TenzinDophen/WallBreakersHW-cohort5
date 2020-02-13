class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        arr = [x[::-1] for x in arr]
        
        return " ".join(arr)