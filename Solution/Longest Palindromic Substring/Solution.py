class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s : return ""
        if s == s[::-1]: return s
        k = len(s)-1
        i = 0
        while k > 0:
            for i in range(len(s) - k+1):
                windows = s[i:i+k]
                if windows == windows[::-1]:
                    return windows
            k -= 1
        