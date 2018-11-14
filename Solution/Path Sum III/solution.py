# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def dfs(self,root,target):
        if root == None:
            return
        self.test(root,target)
        self.dfs(root.left,target)
        self.dfs(root.right,target)
    
    def test(self, root, target):
        if root == None:
            return
        elif root.val == target:
            self.res += 1
        self.test(root.left, target - root.val)
        self.test(root.right, target - root.val)
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.res = 0
        self.dfs(root,sum)
        return self.res