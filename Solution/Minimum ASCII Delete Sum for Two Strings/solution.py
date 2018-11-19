class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        n = len(s1)
        m = len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,len(dp[0])):
            dp[0][i] = ord(s1[i-1])+dp[0][i-1]
        for j in range(1,len(dp)):
            dp[j][0] = ord(s2[j-1])+dp[j-1][0]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s2[i-1] == s1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+ord(s2[i-1]), dp[i][j-1]+ord(s1[j-1]))
        return dp[-1][-1]
        # return dp
                
        