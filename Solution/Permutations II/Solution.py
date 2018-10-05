import itertools
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in itertools.permutations(nums):
            if not i in res:
                res.append(i)
        return res