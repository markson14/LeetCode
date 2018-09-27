class Solution:
    """
        time: O(n)
        space: O(1)
        仅需要遍历一次，若sum大于等于target，从左边开始删除直到sum小于target，继续遍历。
        用一个length保存最短的连续子序列的长度
    """
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sum_ = left = 0
        length = len(nums)+1
        for right,v in enumerate(nums):
            sum_ += v
            while sum_ >= s:
                length = min(length, right - left + 1)
                print(length)
                sum_ -= nums[left]
                left += 1
        return length if length <= len(nums) else 0