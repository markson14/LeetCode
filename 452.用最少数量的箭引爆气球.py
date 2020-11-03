#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda x: x[1])
        count = 1
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= end:
                continue
            end = points[i][1]
            count += 1
        return count
# @lc code=end

