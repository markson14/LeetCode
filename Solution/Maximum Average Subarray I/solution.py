class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        pre = [0]
        max_ = -float('INF')
        for num in nums:
            pre.append(pre[-1]+num)
        for i in range(len(nums)-k+1):
            max_ = max(max_, (pre[i+k]-pre[i])/k)
        return max_