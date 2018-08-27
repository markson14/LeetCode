class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        pad = [[0]*n for _ in range(m)]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j] == 0:
                    if i == m-1 and j == n-1:
                        pad[i][j] = 1
                    if i+1 < m:
                        pad[i][j] += pad[i+1][j]
                    if j+1 < n:
                        pad[i][j] += pad[i][j+1]
                        
        return pad[0][0]