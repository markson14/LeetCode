class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(),ch.lower()]]
            else:
                res = [j+ch for j in res]
        return res