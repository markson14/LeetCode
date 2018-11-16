class Solution:
    def helper(self,s,l,r):
        while l>=0 and r < len(s) and s[l]==s[r]:
            r+=1
            l-=1
        return s[l+1:r]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            tmp = self.helper(s,i,i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.helper(s,i,i+1)
            if len(tmp) > len(res):
                res = tmp
        return res