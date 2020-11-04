#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        left, right = intervals[0][0], intervals[0][1]
        res = []
        for inter in intervals[1:]:
            if left <= inter[0] and right >= inter[1]:
                continue
            if right >= inter[0] and right <= inter[1]:
                right = inter[1]
            if right <= inter[0]:
                res.append([left, right])
                left = inter[0]
                right = inter[1]

        res.append([left,right])
        return res
# @lc code=end

