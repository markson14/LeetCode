import itertools
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1,n+1)]
        return [i for i in itertools.combinations(nums,k)]