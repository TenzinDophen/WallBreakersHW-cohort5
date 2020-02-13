class Solution:
    
    def checkBoundary(self, grid, row, col):
        if 0<= row < len(grid) and 0<= col < len(grid[0]):
            return True
        return False
    
    def bfs(self, grid, row, col , visited):

        boundary = [(0,1), (1,0), (-1,0), (0,-1)]
        friends= [(row,col)]
        while(friends):
            rowPop, colPop = friends.pop()
            visited.add((rowPop, colPop))
            for row, col in boundary:
                newRow = rowPop + row
                newCol = colPop + col

                if self.checkBoundary(grid, newRow, newCol) and (newRow, newCol) not in visited and grid[newRow][newCol] == '1':
                    friends.append((newRow, newCol))
    
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visited and grid[i][j] == '1':
                    result += 1
                    self.bfs(grid, i, j, visited)
                    
        return result