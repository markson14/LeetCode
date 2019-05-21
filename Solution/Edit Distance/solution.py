class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)+1
        m = len(word2)+1
        pad = [[0]*m for _ in range(n)]
        for i in range(m):
            pad[0][i] = i
        for j in range(n):
            pad[j][0] = j
        temp = None
        for i in range(1,n):
            for j in range(1,m):
                if word1[i-1] == word2[j-1]:
                    temp = 0
                else:temp = 1
                pad[i][j] = min(pad[i-1][j]+1,pad[i][j-1]+1,pad[i-1][j-1]+temp)
        return pad[-1][-1]