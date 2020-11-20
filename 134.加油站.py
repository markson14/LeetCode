#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 如果cost大于gas，则无法环游一周
        if sum(gas) < sum(cost):
            return -1
        balance = 0
        start = 0
        for i in range(len(gas)):
            # 当前余额
            balance += gas[i] - cost[i]
            # 当前余额<0，则无法环游一周，可以从i+1开始继续尝试
            if balance < 0:
                balance = 0
                start = i+1
        return start

# @lc code=end

