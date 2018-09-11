class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(x,y,pad):
            if x<0 or y<0 or x>=n or y>=m or pad[x][y] != '1': return
            pad[x][y] = '0'
            dfs(x-1,y,pad)
            dfs(x,y-1,pad)
            dfs(x+1,y,pad)
            dfs(x,y+1,pad)
        
        if not grid: return 0
        
        m = len(grid[0])
        n = len(grid)
        c = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i,j,grid)
                    c += 1
        return c