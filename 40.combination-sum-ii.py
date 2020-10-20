#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def dfs(self, can, idx, tar, path, res):
        if not tar:
            res.append(path)
        for i in range(idx, len(can)):
            if i > idx and can[i] == can[i-1]:
                continue
            
            if can[i] > tar:
                break

            self.dfs(can, i+1, tar-can[i], path+[can[i]], res)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, 0, target, [], res)
        return res

# @lc code=end

