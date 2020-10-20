#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0
        firstmatch = len(s) > 0 and (p[0] == s[0] or p[0] == '.')
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (firstmatch and self.isMatch(s[1:], p))
        else:
            return firstmatch and self.isMatch(s[1:], p[1:])

# @lc code=end
