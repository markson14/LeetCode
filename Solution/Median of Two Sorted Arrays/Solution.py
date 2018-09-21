class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        # return len(nums)//2
        if len(nums) % 2 != 0:
            return nums[len(nums)//2]
        else:
            median = (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2
            return median