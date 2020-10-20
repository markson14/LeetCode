#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        r, ans = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while r+1 < n and s[r+1] not in occ:
                occ.add(s[r+1])
                r += 1
            ans = max(ans, r-i+1)

        return ans


# @lc code=end

