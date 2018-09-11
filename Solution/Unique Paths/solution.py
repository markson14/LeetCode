class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n ==1 or m ==1:
            return 1
        p = [[1] * m] * n
        for i in range(1,n):
            for j in range(1,m):
                p[i][j] = p[i-1][j] + p[i][j-1]
        return p[i][j]