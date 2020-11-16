#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] 将 x 减到 0 的最小操作数
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        '''
        题目可以看成确定最长子序列，且和为sum(nums)-x
        用滑动窗口可以解决
        '''
        left, right = 0,0
        m,n,s = -1, len(nums),sum(nums)-x
        cur = 0
        while right < n:
            cur += nums[right]
            right += 1

            if cur == s:
                m = max(m, right-left)
            
            while cur > s and left < n:
                cur -= nums[left]
                left += 1
            
            if cur == s:
                m = max(m, right-left)
        
        return -1 if m == -1 else n-m
# @lc code=end

