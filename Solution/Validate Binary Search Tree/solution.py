# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        l = []
        def inorder(x,l):
            if x.left: inorder(x.left,l)
            l.append(x.val)
            if x.right:inorder(x.right,l)
        if not root: return True
        inorder(root,l)
        return l == sorted(list(set(l)))