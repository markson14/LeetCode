#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        end, fur, count = 0,0,0
        for i in range(len(nums)-1):
            fur = max(nums[i]+i, fur)
            if end == i:
                count += 1
                end = fur
        return count
                
# @lc code=end

