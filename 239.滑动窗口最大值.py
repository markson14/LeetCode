#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from collections import deque


class MonoticWindows():
    def __init__(self):
        self.queue = deque()

    def push(self, n):
        while self.queue and self.queue[-1] < n:
            self.queue.pop()
        self.queue.append(n)

    def max(self):
        return self.queue[0]

    def remove(self, n):
        if n == self.max():
            self.queue.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        win = MonoticWindows()
        for i in range(len(nums)):
            if i < k-1:
                win.push(nums[i])
            else:
                win.push(nums[i])
                res.append(win.max())
                win.remove(nums[i-k+1])
        return res

# @lc code=end
