class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dic = {c:i for i,c in enumerate(S)}
        res = []
        l,r = 0,0
        for i,v in enumerate(S):
            r = max(r, dic[v])
            if i == r:
                res.append(i - l + 1)
                l = r+1
        return res
       