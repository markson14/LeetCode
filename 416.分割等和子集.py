#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False
        sum_ //= 2
        # sum_+1是因为要取到sum_+1
        dp = [[False for _ in range(sum_+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        for i in range(1, n):
            for j in range(1, sum_+1):
                if j - nums[i] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        # print(dp)
        return dp[-1][-1]
# @lc code=end

