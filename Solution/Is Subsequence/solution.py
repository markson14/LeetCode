class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for char in s:
            i = t.find(char)
            if i == -1:
                return False
            t = t[i+1:]
        return True