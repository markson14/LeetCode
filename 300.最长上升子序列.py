#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        状态：dp[当前index结尾的sequence]=最长长度
        选择：是否选择当前index
        '''
        n = len(nums)
        dp = [1]*n
        if not dp: return 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


# @lc code=end
