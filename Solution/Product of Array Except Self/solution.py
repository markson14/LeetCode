class Solution:
    """
        time: O(n)
        space: O(n)
        先从前往后乘一遍，然后在从后往前乘一遍
    """
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] + [0 for _ in range(len(nums)-1)]
        for i in range(1,len(nums)):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= right
            print(res,right)
            right *= nums[i]
        return res