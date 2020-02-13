class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryOn = 0
        size = len(digits)
        digits.append(0) #[1,2,3] [1,2,3,4]
        
        for i in range(size-1, -1,-1):
            if i == size-1:
                total = digits[i] + 1
            else:
                total = digits[i] + carryOn
            carryOn = total // 10
            rem = total % 10
            digits[i+1] = rem
            
        if carryOn != 0:
            digits[0] = carryOn
            return digits
        
        return digits[1:]
            