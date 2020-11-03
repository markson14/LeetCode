#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        further = 0
        for i in range(n-1):
            further= max(further, i+nums[i])
            if further <= i:
                return False
        return further >= n-1
# @lc code=end

