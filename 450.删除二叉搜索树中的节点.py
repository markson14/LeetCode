#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def get_min(node):
            while node.left:
                node = node.left
            return node

        if not root: return None
        if root.val == key:
            # 处理1.两边无子节点 2.只有一边有子节点
            if not root.left: return root.right
            if not root.right: return root.left
            # 搜索root.right数的最小值替代当前root.val
            min_node = get_min(root.right)
            root.val, min_node.val = min_node.val, root.val
            # 将需要删除节点改为替换后的min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        return root

        
# @lc code=end

