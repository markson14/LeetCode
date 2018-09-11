class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        cur = [root]
        ans = []
        while cur:
            ans.append([node.val for node in cur])
            nxt = []
            for node in cur:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            cur = nxt
        return ans


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
    此方法为试用树结构，上面一个仅限二叉树
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return []
        cur = [root]
        ans = []
        while cur:
            ans.append([node.val for node in cur])
            cur = [child for node in cur for child in node.children if child]
        return ans
        