class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        else:
            if sorted(nums)[-1] >= 2*(sorted(nums)[-2]):
                return nums.index(sorted(nums)[-1])
            return -1