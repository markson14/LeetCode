class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dic = {}
        for i,v in enumerate(order):
            dic[v] = i
        res = []
        for word in words:
            s = []
            for c in word:
                s.append(dic[c])
            res.append(s)
        return res == sorted(res)