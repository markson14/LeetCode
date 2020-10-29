#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(nums):
            n = len(nums)
            dp = [0] * n
            if not dp:
                return 0
            dp[0] = nums[0]
            if n == 1:
                return dp[-1]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            return dp[-1]
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums)
        return max(_rob(nums[1:]), _rob(nums[:-1]))
# @lc code=end

