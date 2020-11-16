#
# @lc app=leetcode.cn id=1648 lang=python3
#
# [1648] 销售价值减少的颜色球
#

# @lc code=start
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort()
        same = 1
        max_ = inventory.pop()
        res = 0
        while orders > 0:
            cur = inventory.pop()
            if orders >= same*(max_-cur):
                res += same*(sum(range(max_+1, cur, -1)))
                orders -= same*(max_-cur)
            else:
                res += 



# @lc code=end
