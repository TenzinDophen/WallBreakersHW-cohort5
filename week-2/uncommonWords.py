from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        result = []
        
        mappingA = defaultdict(int)
        mappingB = defaultdict(int)
        
        for word in A.split(" "):
            mappingA[word] += 1
        
        for word in B.split(" "):
            mappingB[word] += 1
            
        for maps in mappingA:
            if maps not in mappingB and mappingA[maps] == 1:
                result.append(maps)
        
        for maps in mappingB:
            if maps not in mappingA and mappingB[maps] == 1:
                result.append(maps)
                
        return result