class Solution:
    def helper(self, num):
        temp = num # 128
        while(temp != 0):
            mod = temp % 10 

            if mod == 0 or num % mod != 0:
                return False
            temp = temp // 10  #12
        return True
                
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            if self.helper(i):
                result.append(i)
                
        return result