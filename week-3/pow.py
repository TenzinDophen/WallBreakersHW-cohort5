class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n<0:
            x=1/x
            n=-n
        
        return self.helper(x, n)
    
    def helper(self, x, n):
        
        if n == 0:
            return 1
        if n == 1:
            return x
        
        temp = self.helper(x, n//2)
        
        if n % 2 == 0:
            return temp * temp 
        return temp * temp * x