class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last1,last2,now1,now2 = 0,0,0,0
        if len(nums) == 1:
            return nums[0]
        for i in nums[:-1]:
            last1, now1 =now1, max(last1+i, now1)
        for i in nums[1:]:
            last2, now2 =now2, max(last2+i, now2)
        now = max(now1,now2)
        return now