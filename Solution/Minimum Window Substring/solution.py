class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s and t: return ""
        res = float('inf'),None,None
        l,r = 0,0
        formed = 0
        t_count = collections.Counter(t)
        required = len(t_count)
        s_count = {}
        while r < len(s):
            char = s[r]
            s_count[char] = s_count.get(char,0)+1
            if char in t_count and t_count[char] == s_count[char]:
                formed += 1
            while l<=r and formed == required:
                char = s[l]
                if res[0] > r-l+1:
                    res = r-l+1,l,r
                s_count[char] -= 1
                if char in t_count and t_count[char] > s_count[char]:
                    formed -= 1
                l+=1
            r+=1
        return '' if res[0] == float('inf') else s[res[1]:res[2]+1]
                