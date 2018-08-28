class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = len(nums)-1
        for i in reversed(range(last+1)):
            if i+nums[i] >= last:
                last = i
        return last == 0