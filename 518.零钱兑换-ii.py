#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0 for _ in range(amount+1)]
        if not dp: return 0
        # base case
        dp[0] = 1
        for i in range(n):
            for j in range(1, amount+1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j-coins[i]]
        # print(dp)
        return dp[-1]
        
# @lc code=end

