class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        res = 0
        char = {}
        for right in range(len(s)):
            if s[right] in char:
                left = max(left ,char[s[right]]+1)
            char[s[right]] = right
            res = max(right-left+1, res)
        return res
                
            