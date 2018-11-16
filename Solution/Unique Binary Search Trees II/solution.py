# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        def helper(l,r):
            if l>r:
                return [None]
            all_tree = []
            for i in range(l,r+1):
                left_tree = helper(l,i-1)
                right_tree = helper(i+1,r)
            
                for j in left_tree:
                    for k in right_tree:
                        cur = TreeNode(i)
                        cur.left = j
                        cur.right = k
                        all_tree.append(cur)
            return all_tree
        
        return helper(1,n) if n else []