class Solution:
    """
        动态规划，构造相同的dp矩阵。
        难度：Medium
        Time:O(mn)
        Space:O(mn)
    """
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        max_ = 0
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(min(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1])+1
                    max_ = max(max_,dp[i][j])
        return max_ ** 2
        # return dp