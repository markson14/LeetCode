#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for r in range(1, m):
            dp[0][r] = dp[0][r-1] * (1 - obstacleGrid[0][r])
        for c in range(1, n):
            dp[c][0] = dp[c-1][0] * (1 - obstacleGrid[c][0])

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * (1 - obstacleGrid[i][j])

        return dp[-1][-1]
# @lc code=end
