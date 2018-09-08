# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def tobot(x,l):
            if x.left or x.right: 
                if x.left: tobot(x.left,l)
                if x.right: tobot(x.right,l)
            else: l.append(x.val)
        l1 = []
        l2 = []
        tobot(root1,l1)
        tobot(root2,l2)
        return l1 == l2