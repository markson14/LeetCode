# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        l = []
        def inorder(x):
            if x.left: inorder(x.left)
            l.append(x.val)
            if x.right: inorder(x.right)
        inorder(root)
        head = a = TreeNode(-1)
        for i in range(len(l)):
            a.right = TreeNode(l[i])
            a = a.right
        return head.right