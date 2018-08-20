 # Solution 1
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(cur, level):
            if not cur:
                return
            if level not in table:
                table[level] = cur.val
            dfs(cur.right, level + 1)
            dfs(cur.left, level + 1)

        table = dict()
        dfs(root, 0)
        return [table[k] for k in sorted(table.keys())]



# Solution 2
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        q = [root]
        if not root: return res
        
        while q:
            for i in range(len(q)):
                cur = q.pop(0)
                if i == 0: res.append(cur.val)
                if (cur.right != None): q.append(cur.right)
                if (cur.left != None): q.append(cur.left)
        return res
            