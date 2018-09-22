class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            res.extend([sub + [i] for sub in res])
        out = []
        for j in res:
            if not sorted(j) in out:
                out.append(sorted(j))
        return out