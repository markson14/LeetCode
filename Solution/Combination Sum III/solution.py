import itertools
class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1,10)]
        res = []
        for i in itertools.combinations(nums,k):
            if sum(list(i)) == n:
                res.append(list(i))
        return res