class Solution:
             """
                space:O(m+n)
                判断row和col是否含有0
             """
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix[0])
        n = len(matrix)
        
        col_0 = [1 for i in range(m)]
        row_0 = [1 for i in range(n)]
        
        for i in range(n):
            if 0 in matrix[i]:
                row_0[i] = 0
                
        for i in range(m):
            for j in range(n):
                if matrix[j][i] == 0:
                    col_0[i] = 0
                    break
        for i in range(n):
            for j in range(m):
                matrix[i][j] *= col_0[j] * row_0[i]
                
class Solution:
             """
                space:O(mn)
                bruteforce：
                    建立一个pad帮助分别计算col和row
             """
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix[0])
        n = len(matrix)
        pad = copy.deepcopy(matrix)
        def dfscol(x ,y, pad):
            if x < 0 or y < 0 or x >= n or y >= m or pad[x][y] == '#': return
            pad[x][y] = '#'
            dfscol(x+1, y, pad)
            dfscol(x-1, y, pad)
        
        for i in range(n):
            for j in range(m):
                if pad[i][j] == 0:
                    dfscol(i, j, pad)

        for row in range(n):
            if 0 in matrix[row]:
                matrix[row] = [0 for _ in range(m)]

        for i in range(n):
            for j in range(m):
                if pad[i][j] == '#':
                    matrix[i][j] = 0

