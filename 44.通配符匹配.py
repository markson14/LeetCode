#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
        '?' 可以匹配任何单个字符。
        '*' 可以匹配任意字符串（包括空字符串）。
        两个字符串完全匹配才算匹配成功。

        '''
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            firstmatch = bool(i < len(s)) and p[j] in (s[i], '?', '*')
            # 通配符匹配
            if p[j] == '*':
                # 若s遍历到结尾，则返回结尾与p[j+1]的dp结果
                if i == len(s):
                    return dp(i, j+1)
                # 返回当前s后面字符串与'*'的匹配（匹配任意字符串）或当前s与'*'后面的匹配（匹配空字符串）
                ans = dp(i+1, j) or dp(i, j+1)
            else:
                # 常规case，返回firstmatch和s[i+1],p[j+1]的结果
                ans = firstmatch and dp(i+1, j+1)
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)

# @lc code=end
