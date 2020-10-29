#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#

# @lc code=start
from functools import lru_cache
class Solution:
    '''
    动态规划
    '''
    def superEggDrop(self, K: int, N: int) -> int:
        m = 0
        dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
        while dp[K][m] < N:
            m += 1
            for i in range(1, K+1):
                dp[i][m] = dp[i][m-1] + dp[i-1][m-1] + 1
        return m


# @lc code=end
