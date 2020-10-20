#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = [1 for _ in range(n)]
        length = [1 for _ in range(n)]
        mx = 0
        res = 0
        for i in range(n):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                if length[i] == length[j]+1:
                    cnt[i] += cnt[j]
                elif length[i] < length[j]+1:
                    length[i] = length[j]+1
                    cnt[i] = cnt[j]
            if mx == length[i]:
                res += cnt[i]
            elif mx < length[i]:
                mx = length[i]
                res = cnt[i]
        return res
# @lc code=end
