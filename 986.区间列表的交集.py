#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#

# @lc code=start
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i,j = 0,0  # 初始化双指针
        res = []
        while i < len(A) and j < len(B):
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]
            # 存在相交区间
            if b2 >= a1 and b1 <= a2:
                # 更新
                res.append([max(a1,b1), min(a2,b2)])
            # 指针前进条件
            if b2 > a2:
                i += 1
            else:
                j += 1
        return res
            
# @lc code=end

