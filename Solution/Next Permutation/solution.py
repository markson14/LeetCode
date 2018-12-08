class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i>=0 and nums[i-1] >= nums[i]:
            i-=1
        # print(i)
        if i > 0:
            tmp = nums[i-1]
            j = len(nums)-1
            while j >= 0 and nums[j] <= tmp:
                j-=1
            nums[i-1],nums[j] = nums[j],nums[i-1]
        nums[i:len(nums)] = nums[i:len(nums)][::-1]



