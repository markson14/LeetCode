class Solution:
    """
        time:O(n)
        space:O(1)
        遍历nums，将遍历过的元素赋值为None防止重复遍历。
    """
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            if num is not None:
                start, count = num,0
                while nums[start] is not None:
                    tmp = start
                    start = nums[start]
                    nums[tmp] = None
                    count += 1
                res = max(count,res)
        return res
                    