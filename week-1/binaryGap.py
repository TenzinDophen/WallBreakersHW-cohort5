class Solution:
    def intToBin(self, num):
        binStr = ""
        while(num != 0):
            mod = num % 2
            binStr += str(mod)
            num = num // 2
        
        return binStr[::-1]
    
    def binaryGap(self, N: int) -> int:
        binStr = self.intToBin(N)
        longest = 0 
        start = -1 
        
        for i, c in enumerate(binStr):
            if c == "1":
                if start != -1:
                    longest = max(longest, (i-start))
                start = i
        return longest