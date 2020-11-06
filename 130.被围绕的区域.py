#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class UF():
    def __init__(self, n):
        self.count = n
        self.parent = [0]*n
        for i in range(n):
            self.parent[i] = i

    def union(self, p, q):
        """
        union
        """
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        self.parent[p] = q
        self.count -= 1

    def find(self, p):
        """
        find
        """
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def connected(self, p, q):
        """
        connected
        """
        rootp = self.find(p)
        rootq = self.find(q)
        return rootp == rootq


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        uf = UF(m*n+1)
        # x*n + y
        dummy = n*m
        for i in range(n):
            if board[0][i] == 'O':
                uf.union(i, dummy)
            if board[m-1][i] == 'O':
                uf.union(n*(m-1) + i, dummy)
        for j in range(m):
            if board[j][0] == 'O':
                uf.union(j*n, dummy)
            if board[j][n-1] == 'O':
                uf.union(j*n+(n-1), dummy)

        for r in range(1, m-1):
            for c in range(1, n-1):
                if board[r][c] == 'O':
                    for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        x = i + d[0]
                        y = j + d[1]
                        if board[x][y] == 'O':
                            uf.union(x*n+y, i*n+j)
        
        for i in range(m):
            for j in range(n):
                if not uf.connected(i*n+j, dummy):
                    board[i][j] = 'X'
        
# @lc code=end
