#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n)]
        if not dp:
            return 0
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            if i == 1:
                dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
            else:
                dp[i][1] = max(dp[i-2][0]-prices[i], dp[i-1][1])
        
        return dp[-1][0]
# @lc code=end

