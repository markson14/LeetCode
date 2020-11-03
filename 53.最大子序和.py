#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        if not dp: return 0
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i]+dp[i-1])
        
        return max(dp)
# @lc code=end

