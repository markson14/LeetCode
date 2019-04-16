# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, a, b):
            if node:
                a, b = min(a, node.val), max(b, node.val)
                self.ans = max(self.ans, b-a)
                dfs(node.left, a, b), dfs(node.right, a, b)
        dfs(root, float('inf'), float('-inf'))
        return self.ans