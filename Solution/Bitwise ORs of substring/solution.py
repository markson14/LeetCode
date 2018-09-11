class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cur = set()
        res = set()
        for a in A:
            cur = {a | b for b in cur}| {a}
            res |= cur
        return len(res)