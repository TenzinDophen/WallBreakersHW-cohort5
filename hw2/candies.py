class Solution:
    
    def getKinds(self, candies):
        setA = set()
        for i in candies:
            setA.add(i)
        return len(setA)
            
        
        
    def distributeCandies(self, candies: List[int]) -> int:
        
        return min(len(candies) // 2, self.getKinds(candies))