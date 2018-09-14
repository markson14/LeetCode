class Solution(object): # 1384ms
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        res = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    res[i] = max(res[i],res[j]+1)
        return max(res)

class Solution:
    """
        time: n
        space n
    """
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        res = [1] * len(nums)
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1] > 0:
                res[i] = res[i-1]+1
        return max(res)
            
