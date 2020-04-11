class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
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


class Solution(object):
    """
    reverse traversal
    """

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
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
        return ans[::-1]


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cur = [root]
        res = []
        tag = 1
        while cur:
            if tag == 1:
                res.append(node.val for node in cur)
            else:
                res.append(node.val for node in cur[::-1])
            nxt = []
            for node in cur:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            cur = nxt
            if tag == 1:
                tag = 0
            else:
                tag = 1

        return res


class Solution(object):
    """
    # Definition for a Node.
    class Node(object):
        def __init__(self, val, children):
            self.val = val
            self.children = children
        此方法为试用树结构，上面一个仅限二叉树
    """

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        cur = [root]
        ans = []
        while cur:
            ans.append([node.val for node in cur])
            cur = [child for node in cur for child in node.children if child]
        return ans


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        cur = [root]
        ans = []
        while cur:
            tmp = [node.val for node in cur]
            ans.append(sum(tmp)/len(tmp))
            tmp = []
            nxt = []
            for node in cur:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            cur = nxt
        return ans
