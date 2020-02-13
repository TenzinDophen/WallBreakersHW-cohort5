from collections import defaultdict
class Solution:
    
    
    def findFriends(self, num , mapping, visited):
        queue = [num]

        while(queue):
            n = queue.pop()
        
            visited.add(n)
            for i in mapping[n]:
                if i not in visited:
                    queue.append(i)
        

            
            
    def findCircleNum(self, M: List[List[int]]) -> int:
        result = 0
        visited = set()
        
        mapping = defaultdict(list)
        
        for i in range(len(M)):
            for j in range(len(M[i])):
                if i != j and  M[i][j] == 1:
                    mapping[i].append(j)
        
        
        for i in range(len(M)):
            if i not in visited:
                result += 1
                self.findFriends(i, mapping, visited)
               
                
        return result