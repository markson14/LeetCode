class Solution(object):
"""
同时遍历两个list，若小孩贪心满足蛋糕大小，res+=1；否则，蛋糕列表+=1向后遍历。
"""
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        m,n = len(g),len(s)
        res,i,j = 0,0,0
        while i < m and j < n:
            if g[i] <= s[j]:
                i+=1
                j+=1
                res+=1
            else:
                j+=1
        return res
        