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
        # 初始化单调窗口
        win = MonoticWindows()
        for i in range(len(nums)):
            if i < k-1:
                win.push(nums[i])
            else:
                # 将当前推入窗口
                win.push(nums[i])
                # 添加窗口max值
                res.append(win.max())
                # 如果移除单调窗口最左侧值
                win.remove(nums[i-k+1])
        return res

# @lc code=end
