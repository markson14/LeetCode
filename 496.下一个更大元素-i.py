#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        n = len(nums1)
        res = [0] * len(nums2)
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            res[i] = -1 if not stack else stack[-1]
            stack.append(nums2[i])
        op = []
        for a in nums1:
            op.append(res[nums2.index(a)])
        return op
        
# @lc code=end

