#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 遍历到空节点，新建并返回
        if not root: 
            return TreeNode(val)
        # 向右节点遍历
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        # 向左节点遍历
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        return root
        
# @lc code=end

