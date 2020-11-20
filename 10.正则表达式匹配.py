#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
        '.' 匹配任意单个字符
        '*' 匹配零个或多个前面的那一个元素
        所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
        '''
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
                # 发现通配符'*', 匹配当前s与通配符后字符串(匹配零个) 或 匹配当前s后一位和通配符（匹配多个前面一个元素）
                ans = dp(i, j+2) or firstmatch and dp(i+1, j)
            # 常规匹配
            else:
                ans = firstmatch and dp(i+1, j+1)
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)
# @lc code=end
