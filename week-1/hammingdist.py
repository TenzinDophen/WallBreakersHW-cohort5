class Solution:
    
    def intToBin(self, num):
        binStr = ""
        while(num != 0):
            mod = num % 2
            binStr += str(mod)
            num = num // 2
        print("s",binStr)
        return binStr[::-1]
            
            
    def hammingDistance(self, x: int, y: int) -> int:
       
        s1 = self.intToBin(x)
        s2 = self.intToBin(y)
        c1 = len(s1)-1
        c2 = len(s2)-1
        res = 0
        
        while(c1 >= 0 and c2 >= 0):
            if s1[c1] != s2[c2]:
                res += 1
            c1 -= 1
            c2 -= 1
        
        while(c1 >= 0):
            if s1[c1] == "1":
                res += 1
            c1 -= 1
            
        while(c2 >= 0):
            if s2[c2] == "1":
                res += 1
            c2 -= 1
            
        return res