#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # print(inorder, postorder)
        if not inorder:
            return None
        root = TreeNode()
        root.val = postorder[-1]
        idx = inorder.index(root.val)

        left_chunk_sz = len(inorder[:idx])
        right_chunk_sz = len(inorder[idx+1:])

        root.left = self.buildTree(inorder[:idx], postorder[:left_chunk_sz])
        root.right = self.buildTree(
            inorder[idx+1:], postorder[left_chunk_sz:left_chunk_sz+right_chunk_sz])

        return root
# @lc code=end
