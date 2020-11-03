#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3: return False
        max_ = A.index(max(A))
        left = max_ - 1
        right = max_ + 1
        if max_ == 0 or max_ == len(A)-1:
            return False
        while left >= 0 and right < len(A):
            if A[left] < A[left+1] and A[right] < A[right-1]:
                left -= 1
                right += 1
            else:
                return False
        while left >= 0:
            if A[left] < A[left+1]:
                left -= 1
            else:
                return False
        while right < len(A):
            if A[right] < A[right-1]:
                right += 1
            else:
                return False
        return True

        
        
# @lc code=end

