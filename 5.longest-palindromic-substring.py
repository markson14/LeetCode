#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def center_expand(self, l, r):
        while l >= 0 and r < self.n and self.s[l] == self.s[r]:
            l -= 1
            r += 1
        return l+1, r-1
    def longestPalindrome(self, s: str) -> str:
        self.n = len(s)
        self.s = s

        left, right = 0,0
        for i in range(self.n):
            left1, right1 = self.center_expand(i,i)
            left2, right2 = self.center_expand(i,i+1)

            if right1-left1 > right-left:
                left = left1
                right = right1
            if right2-left2 > right-left:
                left = left2
                right = right2
        
        return s[left:right+1]
# @lc code=end

