# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        res= []
        def search(root):
            if root == None:
                return
            if L <= root.val <= R:
                res.append(root.val)
            search(root.left)
            search(root.right)
        search(root)
        return sum(res)