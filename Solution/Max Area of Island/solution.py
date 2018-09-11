class Solution(object):
    
    def dfs(self,x,y,grid):
            if x>=self.m or y>=self.n or x<0 or y<0 or grid[x][y]!=1: return
            grid[x][y] = 0
            self.area += 1
            self.dfs(x-1,y,grid)
            self.dfs(x+1,y,grid)
            self.dfs(x,y-1,grid)
            self.dfs(x,y+1,grid)
    
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        """
        self.area = 0
        self.m = len(grid)
        self.n = len(grid[0])
        
        max_ = 0
        area = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.dfs(i,j,grid)
                    max_ = max(self.area,max_)
                    self.area=0
        return max_