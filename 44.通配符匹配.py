#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
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
            firstmatch = bool(i < len(s)) and p[j] in (s[i], '?', '*')
            # 通配符匹配
            if p[j] == '*':
                # 若s遍历到结尾，则返回结尾与p[j+1]的dp结果
                if i == len(s):
                    return dp(i, j+1)
                # 返回通配符与s[i]以后字符串的结果和通配符后一个字符与当前s[i]的结果
                ans = dp(i+1, j) or dp(i, j+1)
            else:
                # 常规case，返回firstmatch和s[i+1],p[j+1]的结果
                ans = firstmatch and dp(i+1, j+1)
            memo[(i,j)] = ans
            return ans
        return dp(0,0)
            
# @lc code=end

