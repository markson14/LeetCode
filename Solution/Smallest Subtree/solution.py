class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def deep(root):
            if not root:
                return (None,0)
            l,r = deep(root.left),deep(root.right)
            if l[1] > r[1]: return (l[0],l[1]+1)
            elif l[1] < r[1]: return (r[0],r[1]+1)
            else: return (root,l[1]+1)
        return deep(root)[0]
