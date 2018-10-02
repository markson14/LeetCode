class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        tmp = [[0]*n for _ in range(n)]
        for j in range(n):
            for i in range(n-1,-1,-1):
                tmp[j][n-i-1] = matrix[i][j]
        for k in range(n):
            matrix[k] = tmp[k]
        
                