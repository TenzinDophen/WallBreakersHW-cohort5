class Solution:
    def findComplement(self, num: int) -> int:
        binStr = ""
        
        while(num != 0):
            mod = num % 2
            if mod == 1:
                mod = 0
            else:
                mod = 1
            binStr += str(mod)
            num //= 2
            
        binStr = binStr[::-1]
        
        total = 0
        size = len(binStr)-1
        for i in range(size, -1, -1):
            total = total +  (pow(2, (size-i)) * int(binStr[i]))
        
        return total