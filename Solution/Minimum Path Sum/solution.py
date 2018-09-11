class Solution(object): # 80ms
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        for i in range(0,n):
            for j in range(0,m):
                if j==0 and i ==0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = min(grid[i][j] + grid[i][j-1],grid[i][j] + grid[i-1][j])
        return grid[n-1][m-1]


class Solution(object): # 32ms
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, len(grid)):
            for j in range(1,len(grid[0])):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]