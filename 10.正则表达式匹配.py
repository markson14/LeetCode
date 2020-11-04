#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            # 首字符匹配
            firstmatch = bool(i < len(s)) and p[j] in (s[i], '.')
            # 通配符匹配
            if j <= len(p)-2 and p[j+1] == '*':
                # 发现通配符'*', text与pattern
                ans = dp(i, j+2) or firstmatch and dp(i+1, j)
            # 常规匹配
            else:
                ans = firstmatch and dp(i+1, j+1)
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)
# @lc code=end
