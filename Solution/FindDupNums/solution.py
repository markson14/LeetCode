class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i])-1] *= (-1)