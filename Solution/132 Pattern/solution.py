class Solution(object):
    """
        Time Complexity: O(N)
    """
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        stack = []
        s3 = -float('inf')
        for n in nums[::-1]:
            if s3 > n:
                return True
            else:
                while stack and n > stack[-1]:
                    s3 = stack.pop()
            stack.append(n)
        return False


class Solution(object):
    """
        Time Complexity: O(N^2)
        TLE
    """
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3: return False
        for i in range(n):
            max_ = -float('inf')
            for j in range(i+1,n):
                if max_ < nums[j]: max_ = nums[j]
                if max_>nums[j] and max_>nums[i] and nums[j]>nums[i]:
                    return True
        return False
