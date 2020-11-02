#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
import numpy as np
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        状态：dp[当前word1字母][当前word2字母] = 最小编辑距离
        选择：插入，删除，替换，无操作
        '''
        m = len(word1)
        n = len(word2)
        dp = np.zeros((m+1, n+1)).tolist()
        if not len(dp): return 0
        # base case
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 当前字母相等，可以不做任何操作
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # 反之，取3个选择中编辑距离最小的+1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        # print(dp)
        return dp[-1][-1]
        
# @lc code=end

