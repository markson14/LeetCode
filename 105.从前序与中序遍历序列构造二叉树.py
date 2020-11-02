#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not preorder:
            return None
        root = TreeNode()
        root.val = preorder[0]
        idx = inorder.index(root.val)

        left_chunk_size = len(inorder[:idx])
        right_chunk_size = len(inorder[idx+1:])

        root.left = self.buildTree(preorder[1:1+left_chunk_size], inorder[:idx])
        root.right = self.buildTree(
            preorder[left_chunk_size+1: left_chunk_size+right_chunk_size+1], inorder[idx+1:])
        return root


# @lc code=end
