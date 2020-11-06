#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, min_, max_):
            if not root: return True
            if min_ != None and root.val <= min_.val: return False
            if max_ != None and root.val >= max_.val: return False
            return helper(root.left, min_, root) and helper(root.right, root, max_)
        return helper(root, None, None)

# @lc code=end

