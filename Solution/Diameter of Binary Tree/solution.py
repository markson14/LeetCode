# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 1
        def depth(root):
            if root == None:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            self.res = max(self.res, l+r+1)
            return max(l,r)+1
        depth(root)
        return self.res-1