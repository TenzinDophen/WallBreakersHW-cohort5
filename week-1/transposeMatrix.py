class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = [[0 for _ in range(len(A))]  for _ in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                result[j][i] = A[i][j]
                
                
        return result