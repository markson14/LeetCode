class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        l = [i for i in range(len(S)+1)]
        for s in S:
            if s == 'I':
                res.append(l.pop(0))
            else:
                res.append(l.pop())
        return res + l