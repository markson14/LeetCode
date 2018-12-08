class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo,hi = 0,len(nums)-1
        while lo < hi:
            mi = (lo+hi)//2
            if nums[mi] == target:
                return mi
            elif nums[mi] > nums[hi]:
                lo = mi+1
            else:
                hi = mi
        bias = lo # 计算偏置项
        l,r = 0,len(nums)-1
        while l<=r:
            mi = (l+r)//2
            rm = (mi+bias)%len(nums)
            if nums[rm] == target:
                return rm
            elif nums[rm] < target:
                l = mi + 1
            else:
                r = mi - 1
        return -1
        
                