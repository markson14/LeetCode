#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def twoSumTarget(self, nums, target):
        # nums 数组必须有序
        lo, hi = 0, len(nums)-1
        res = []
        while lo < hi:
            # 当前和
            sum_ = nums[lo] + nums[hi]
            left = nums[lo]
            right = nums[hi]
            # 和比target小，则右移lo到下一个不同数字的index
            if sum_ < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
                    # 和比target大，则左移hi到下一个不同数字的index
            elif sum_ > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1
                # 添加[left,right]，并将lo,hi移动至下一个不同数字的index
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return res

    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            tuple_list = self.twoSumTarget(nums[i+1:], target-nums[i])
            # print(tuple_list, nums[i], i)
            for t in tuple_list:
                t.append(nums[i])
            if tuple_list:
                res.extend(tuple_list)
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            tuple_list = self.threeSum(nums[i+1:], target-nums[i])
            # print(tuple_list, nums[i], i)
            for t in tuple_list:
                t.append(nums[i])
            if tuple_list:
                res.extend(tuple_list)
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                print('here')
                i += 1
            i += 1
        return res

        # @lc code=end
