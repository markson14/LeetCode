#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if not n:
            return []
        intervals.sort(key=lambda x: (x[0], -x[1]))
        left, right = intervals[0][0], intervals[0][1]
        res = []
        for inter in intervals[1:]:
            # covered
            if left <= inter[0] and right >= inter[1]:
                continue
            # intersection
            if right >= inter[0] and right <= inter[1]:
                right = inter[1]
            # outside
            if right < inter[0]:
                res.append([left, right])
                left = inter[0]
                right = inter[1]
        res.append([left, right])
        return res
# @lc code=end

