class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums = sorted(nums)
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return True
            elif nums[mid] == nums[l]:
                l+=1
            elif nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
        return False