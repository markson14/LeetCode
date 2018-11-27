class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.dp = [[False]*len(matrix[0]) for _ in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res,self.dfs(matrix,i,j))
        return res
    
    def dfs(self,pad,x,y):
        if self.dp[x][y]:
            return self.dp[x][y]
        n = len(pad)
        m = len(pad[0])
        count = 1
        temp = pad[x][y]
        if x+1 < n and pad[x+1][y] > temp:
            count = max(count,1+self.dfs(pad,x+1,y))
        if y+1 < m and pad[x][y+1] > temp:
            count = max(count,1+self.dfs(pad,x,y+1))
        if x-1 >= 0 and pad[x-1][y] > temp:
            count = max(count,1+self.dfs(pad,x-1,y))
        if y-1 >= 0 and pad[x][y-1] > temp:
            count = max(count,1+self.dfs(pad,x,y-1))
        self.dp[x][y] = count
        return count
        