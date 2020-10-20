#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        cur = {v: 0 for v in t}
        l,r = 0,0
        shortest = 1e9
        res = ''
        while l <= r:
            if 0 in cur.values():
                if s[r] in cur:
                    cur[s[r]] += 1
                    r += 1
                else:
                    r += 1
                    continue
            else:
                if s[l] in cur:
                    cur[s[l]] -= 1
                    l += 1
                else:
                    l += 1
                    continue
            if r-l+1 < shortest:
                res = s[l:r]
        return res
# @lc code=end

