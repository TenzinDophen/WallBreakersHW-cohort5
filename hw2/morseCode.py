from collections import defaultdict
class Solution:
    def getIndex(self, c):
        return ord(c) - ord("a")
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mapping = defaultdict(int)
        
        for word in words:
            morseCode = ""
            for char in word:
                index = self.getIndex(char)
                morseCode += code[index]
            mapping[morseCode] += 1
            
        return len(mapping)