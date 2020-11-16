#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = list()
        for p in people:
            # res.insert(p[1], p)
            res[p[1]:p[1]] = [p]
        return res
        
# @lc code=end

