#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if not n:
            return []
        stack = []
        res = [-1] * n
        for i in range(2*n, -1, -1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if stack:
                res[i%n] = stack[-1]
            stack.append(nums[i%n])

        return res
# @lc code=end

