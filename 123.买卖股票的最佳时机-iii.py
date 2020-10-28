#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0, 0] for _ in range(2+1)] for _ in range(n)]
        if not dp:
            return 0
        for k in range(3):
            dp[0][k][0] = 0
            dp[0][k][1] = -prices[0]
        for i in range(1, n):
            for k in range(1,3):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
                dp[i][k][1] = max(dp[i-1][k-1][0]-prices[i], dp[i-1][k][1])
        return dp[-1][-1][0]
# @lc code=end
