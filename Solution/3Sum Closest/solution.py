class Solution:
    """
        难度：Medium
        变种的3Sum，其实还是固定一个，然后对另外两个进行双指针从两头开始向中间收拢计算
    """
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = float('inf'),None
        for i in range(len(nums)):
            l,r = i+1,len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r] > target:
                    if abs(nums[i]+nums[l]+nums[r] - target) < res[0]:
                        res = abs(nums[i]+nums[l]+nums[r] - target), nums[i]+nums[l]+nums[r]
                    r-=1
                elif nums[i]+nums[l]+nums[r] < target:
                    if abs(nums[i]+nums[l]+nums[r] - target) < res[0]:
                        res = abs(nums[i]+nums[l]+nums[r] - target), nums[i]+nums[l]+nums[r]
                    l+=1
                else:
                    return nums[i]+nums[l]+nums[r]
        return res[1]
                