class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subset = [[]]
        for num in nums:
            subset.extend([sub + [num] for sub in subset])
        return subset
        