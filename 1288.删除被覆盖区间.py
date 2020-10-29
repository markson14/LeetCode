#
# @lc app=leetcode.cn id=1288 lang=python3
#
# [1288] 删除被覆盖区间
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        left, right = intervals[0][0], intervals[0][1]
        res = 0
        for inter in intervals[1:]:
            # 找到覆盖区域
            if left <= inter[0] and right >= inter[1]:
                res += 1
            # 找到相交区域，更新右边界
            if right >= inter[0] and right <= inter[1]:
                right = inter[1]
            # 区域不相交，更新左右边界
            if right < inter[0]:
                left = inter[0]
                right = inter[1]
        return n - res
# @lc code=end

