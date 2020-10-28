#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def match(windows, need):
            for k,v in need.items():
                if windows[k] < v:
                    return False
            return True

        need, windows = defaultdict(int), defaultdict(int)
        for c in t: need[c] += 1
        left, right = 0,0
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                windows[c] += 1

            if match(windows, need):
                return s[left:right]

            while windows[c] > need[c]:
                d = s[left]
                left += 1
                windows[d] -= 1

# @lc code=end

