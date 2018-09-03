"""
set之后，判断cur-1是否在set里。如果不在，则进行+1操作直到停止。这样节省了中间许多重复计算 44ms
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                cur = num
                c = 0
                while cur in nums:
                    cur += 1
                    c += 1
                if longest < c:
                    longest = c
        return longest
