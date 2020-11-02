#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        '''
        x+y = sum, x-y = S
        x = (sum+S)//2
        转换成了求用nums填充满容量为x的背包，总共多少种方法
        状态：dp[当前元素][当前和] = 方法数量
        选择：选择[当前元素]，或者不选
        '''
        x = sum(nums)+S
        if x % 2 != 0 or S > sum(nums):
            return 0
        value = x//2 + 1
        # value+1是为了取得当前值，len(nums)+1是为了取得nums最后一位
        dp = [[0]*value for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for i in range(1, len(nums)+1):
            for j in range(value):
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        return dp[-1][-1]


# @lc code=end
