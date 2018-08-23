class Solution(object): #32 ms
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_ = max_ = res = nums[0]
        for i in range(1,len(nums)):
            
            temp = max_
            max_ = max(max_*nums[i], min_*nums[i], nums[i])
            min_ = min(temp*nums[i], min_*nums[i], nums[i])
            
            res = max(res,max_)
            
        return res