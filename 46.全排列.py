#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, track):
            if len(track) == len(nums):
                res.append(track[::])
            for i in range(len(nums)):
                if nums[i] in track: 
                    continue
                track.append(nums[i])
                backtrack(nums, track)
                track.pop()
        backtrack(nums,[])
        return res

# @lc code=end

