#
# @lc app=leetcode.cn id=514 lang=python3
#
# [514] 自由之路
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m = len(ring)
        n = len(key)
        pos = defaultdict(list)
        for i,v in enumerate(ring):
            pos[v].append(i)
        dp = [[float('INF')] * m for _ in range(n)]
        for idx in pos[key[0]]:
            dp[0][idx] = min(idx, m-idx)+1
        # 当前key的idx
        for i in range(1, n):
            # 当前key的pos
            for j in pos[key[i]]:
                # 上一个key的pos
                for k in pos[key[i-1]]:
                    dp[i][j] =min(dp[i][j], dp[i-1][k] + min(abs(j-k), m-abs(j-k))+1)
        
        print(dp, pos[key[-1]], ring)
        # 最后一位的pos中所有dp的最小值
        return min(dp[n-1])




# @lc code=end
