#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0,0] for _ in range(k+1)] for _ in range(n)]
        if k > n//2:
            dp = [[0, 0] for _ in range(len(prices))]
            if not dp:
                return 0
            dp[0][0] = 0
            dp[0][1] = -prices[0]
            for i in range(1, len(prices)):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
                dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
            return dp[len(prices)-1][0]

        for j in range(k+1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]
        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                dp[i][j][1] = max(dp[i-1][j-1][0]-prices[i], dp[i-1][j][1])
        return dp[-1][-1][0]
# @lc code=end

