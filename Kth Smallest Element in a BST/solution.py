# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        l = []
        def dfs(x,l,k):
            if x.left:  dfs(x.left,l,k)
            l.append(x.val)
            k -= 1
            if k == 0:
                return x.val
            if x.right:  dfs(x.right,l,k)
        return dfs(root,l,k)
            