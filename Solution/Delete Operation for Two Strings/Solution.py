class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: in
        """
        m = len(word1)+1
        n = len(word2)+1
        dp = [[ 0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            dp[0][i] = i
        for j in range(n):
            dp[j][0] = j
        for i in range(1,n):
            for j in range(1,m):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
                