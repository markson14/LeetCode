class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        m,n,res = len(s),set(),set()
        if m < 10:
            return []
        for i in range(m):
            win = s[i:i+10]
            if win in n:
                res.add(win)
            else:
                n.add(win)
        return list(res)
        