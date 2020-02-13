class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        c = 0
        size = len(A)
        while(i < size):
            num = A[c]
            
            if num % 2 != 0:
            
                A.remove(num)
                A.append(num)
            else:
                c += 1
            i += 1
        return A